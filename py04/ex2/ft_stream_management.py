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

    content = ""
    f: IO[str] | None = None
    try:
        f = open(filename, "r")
        content = f.read()
        print("---")
        print(content, end="")
        if content and not content.endswith("\n"):
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

    lines = content.splitlines()
    transformed_content = "".join([line + "#\n" for line in lines])

    print("Transform data:")
    print("---")
    print()
    print(transformed_content, end="")
    print()
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_filename = sys.stdin.readline().strip()

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
