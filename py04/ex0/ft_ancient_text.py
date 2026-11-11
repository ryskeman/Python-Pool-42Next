#!/usr/bin/env python3
import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        print()
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    f: IO[str] | None = None
    try:
        f = open(filename, "r")
        print("---")
        print()
        print(f.read(), end="")
        print()
        print("---")

    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        print()

    finally:
        if f is not None and not f.closed:
            f.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
