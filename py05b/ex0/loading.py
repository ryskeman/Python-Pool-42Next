#!/usr/bin/env python3
import importlib


def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")

    packages: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready"
    }
    all_loaded: bool = True
    for pkg_name, description in packages.items():
        try:
            module = importlib.import_module(pkg_name)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {pkg_name} ({version}) - {description}")

        except ImportError:
            all_loaded = False
            print(f"[MISSING] {pkg_name} - Not installed")

    if all_loaded:
        print("pip vs Poetry:")
        print(
            "requirements.txt declares what to install; "
            "pip resolves it at install time."
        )
        print(
            "pyproject.toml declares the same constraints, "
            "and Poetry pins the resolved"
        )
        print("versions in poetry.lock so every install is identical.")
        print("All reagents present and accounted for.")
        print()
    else:
        print("Missing reagents detected. Install them using:")
        print("pip install -r ex0/requirements.txt")
        print("poetry install")
        print()


if __name__ == "__main__":
    main()
