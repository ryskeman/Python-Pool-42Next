#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Protocol, Sequence


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank: int = 0
        self._total_processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise ValueError("No data available to output.")

        save_data = self._data.pop(0)
        current_rank = self._rank
        self._rank += 1
        return (current_rank, save_data)

    def get_total_processed(self) -> int:
        return self._total_processed

    def get_remaining(self) -> int:
        return len(self._data)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True

        elif isinstance(data, list) and all(
            isinstance(x, (int, float))
            and not isinstance(x, bool) for x in data
        ):
            return True

        else:
            return False

    def ingest(self, data: int | float | Sequence[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._data.append(str(item))
                self._total_processed += 1

        else:
            self._data.append(str(data))
            self._total_processed += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str) or (
            isinstance(data, list) and all(isinstance(x, str) for x in data)
        ):
            return True
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._data.append(str(item))
                self._total_processed += 1

        else:
            self._data.append(str(data))
            self._total_processed += 1


class LogProcessor(DataProcessor):
    def _is_valid_log(self, entry: Any) -> bool:
        return (
            isinstance(entry, dict)
            and all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in entry.items()
            )
            and "log_level" in entry
            and "log_message" in entry
        )

    def validate(self, data: Any) -> bool:
        return self._is_valid_log(data) or (
            isinstance(data, list) and all(self._is_valid_log(x) for x in data)
        )

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            for entry in data:
                msg = f"{entry['log_level']}: {entry['log_message']}"
                self._data.append(msg)
                self._total_processed += 1

        else:
            msg = f"{data['log_level']}: {data['log_message']}"
            self._data.append(msg)
            self._total_processed += 1


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class DataStream():
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(item):
                    proc.ingest(item)
                    handled = True
                    break
            if not handled:
                print(
                    "DataStream error - Can't"
                    f" process element in stream: {item}"
                )

    def print_processors_stats(self) -> None:
        print()
        print("== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
        else:
            for proc in self._processors:
                name = type(proc).__name__.replace("Processor", " Processor")
                total = proc.get_total_processed()
                remaining = proc.get_remaining()
                print(
                    f"{name}: total {total} items processed, "
                    f"remaining {remaining} on processor"
                )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            extracted: list[tuple[int, str]] = []
            for _ in range(nb):
                if proc.get_remaining() > 0:
                    extracted.append(proc.output())
                else:
                    break
            plugin.process_output(extracted)


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [val for _, val in data]
        print("CSV Output:")
        print(",".join(values))


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = [f'"item_{rank}": "{val}"' for rank, val in data]
        print("JSON Output:")
        print(f"{{{', '.join(items)}}}")


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print()
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()
    print()

    print("Registering Processors")
    print()
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch_1 = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ['Hi', 'five']
    ]
    print(f"Send first batch of data on stream: {batch_1}")
    stream.process_stream(batch_1)
    stream.print_processors_stats()
    print()
    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVPlugin())
    stream.print_processors_stats()
    print()

    batch_2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {
                'log_level': 'ERROR',
                'log_message': '500 server crash'
            },
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            }
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(f"Send another batch of data: {batch_2}")
    stream.process_stream(batch_2)
    stream.print_processors_stats()
    print()
    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONPlugin())
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
