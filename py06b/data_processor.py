#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Sequence


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank: int = 0

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

        else:
            self._data.append(str(data))


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

        else:
            self._data.append(str(data))


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

        else:
            msg = f"{data['log_level']}: {data['log_message']}"
            self._data.append(msg)


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()

    print("Testing Numeric Processor...")
    num_proc = NumericProcessor()
    print(f"Trying to validate input '42': {num_proc.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest('foo')
    except ValueError as e:
        print(f"Got exception: {e}")

    num_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")

    num_proc.ingest(num_data)
    print("Extracting 3 values...")
    for _ in range(3):
        _rank, val = num_proc.output()
        print(f"Numeric value {_rank}: {val}")
    print()

    print("Testing Text Processor...")
    text_proc = TextProcessor()
    print(f"Trying to validate input '42': {text_proc.validate(42)}")
    text_data = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {text_data}")
    text_proc.ingest(text_data)
    print("Extracting 1 value...")
    for _ in range(1):
        _rank, val = text_proc.output()
        print(f"Text value {_rank}: {val}")
    print()

    print("Testing Log Processor...")
    log_proc = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")
    log_data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]

    print(f"Processing data: {log_data}")
    log_proc.ingest(log_data)
    print("Extracting 2 values...")
    for _ in range(2):
        _rank, val = log_proc.output()
        print(f"Log entry {_rank}: {val}")
    print()


if __name__ == "__main__":
    main()
