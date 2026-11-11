#!/usr/bin/env python3
import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>", file=sys.stderr)
        print()
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    lines: list[str] = []
    f: IO[str] | None = None
    try:
        f = open(filename, "r")
        lines = f.readlines()
        print("---")
        print()
        for line in lines:
            print(line, end="")
        print()
        print("---")

    except OSError as e:
        print(
            f"[STDERR] Error opening file '{filename}': {e}",
            file=sys.stderr
        )
        return

    finally:
        if f is not None and not f.closed:
            f.close()
            print(f"File '{filename}' closed.")
            print()

    transformed_lines = [line.rstrip("\n") + "#\n" for line in lines]
    transformed_content = "".join(transformed_lines)

    print("Transform data:")
    print("---")
    print()
    print(f"{transformed_content}")
    print()
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_filename = sys.stdin.readline().strip("\n").strip()

    if not new_filename:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")
    out_f: IO[str] | None = None
    try:
        out_f = open(new_filename, "w")
        out_f.write(transformed_content)
        print(f"Data saved in file '{new_filename}'.")
    except OSError as e:
        print(
            f"[STDERR] Error opening file '{new_filename}': {e}",
            file=sys.stderr
        )
        print("Data not saved.")
    finally:
        if out_f is not None and not out_f.closed:
            out_f.close()


if __name__ == "__main__":
    main()
