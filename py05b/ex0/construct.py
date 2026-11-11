#!/usr/bin/env python3
import os
import site
import sys


def main() -> None:
    if sys.prefix != sys.base_prefix:
        env_name = os.path.basename(sys.prefix)
        site_packages = site.getsitepackages()[0]

        print("LABORATORY STATUS: The laboratory is sealed")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.")
        print()
        print("Reagent installation path:")
        print(site_packages)
    else:
        print("LABORATORY STATUS: You are working in the open")
        print()
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print()
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print(r"lab_env\Scripts\activate # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()
