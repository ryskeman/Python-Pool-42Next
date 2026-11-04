#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Command Quest ===")
    total = len(sys.argv)
    print(f" Program name: {sys.argv[0]}")
    if total == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total - 1}")
        for i in range(1, total):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {total}")


if __name__ == "__main__":
    main()
