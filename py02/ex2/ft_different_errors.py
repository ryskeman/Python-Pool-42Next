#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        "plantas: " + 42  # type: ignore[operator]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
            print()
        except (
            ValueError,
            ZeroDivisionError,
            FileNotFoundError,
            TypeError
        ) as e:
            print(f"Caught {e.__class__.__name__}: {e}")
    print("All error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
