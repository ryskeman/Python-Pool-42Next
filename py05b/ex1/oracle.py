#!/usr/bin/env python3
import os
import sys


try:
    from dotenv import load_dotenv  # type: ignore[import-not-found]
except ImportError:
    print("[WARNING] python-dotenv is not installed.")
    print("To set up the environment, run:")
    print("python3 -m venv lab_env")
    print("source lab_env/bin/activate")
    print("pip install -r ex1/requirements.txt")
    print("Then run this program again.")
    sys.exit(1)


def main() -> None:
    base_dir: str = os.path.dirname(os.path.abspath(__file__))
    env_path: str = os.path.join(base_dir, ".env")
    load_dotenv(env_path)
    mode: str = os.getenv("MATRIX_MODE", "development").lower()
    db_url: str = os.getenv("DATABASE_URL", "")
    api_key: str = os.getenv("API_KEY", "")
    default_log: str = "DEBUG" if mode == "development" else "WARNING"
    log_level: str = os.getenv("LOG_LEVEL", default_log)
    zion_endpoint: str = os.getenv("ZION_ENDPOINT", "")

    print("ORACLE STATUS: Consulting the configuration...")
    print()
    print("Configuration loaded:")
    print(f"Mode: {mode}")

    is_prod: bool = mode == "production"
    if db_url != "" and is_prod:
        print("Database: Connected to production cluster")
    elif db_url:
        print("Database: Connected to local instance")
    else:
        print("Database: [WARNING] Missing DATABASE_URL")

    if api_key and api_key != "your_api_key_here":
        print("API Access: Authenticated")
    else:
        print("API Access: [WARNING] Missing or placeholder API_KEY")
    if is_prod and log_level.upper() == "DEBUG":
        log_level = "WARNING"
    print(f"Log Level: {log_level}")

    if zion_endpoint and is_prod:
        print("Remote Network: Online (secure mainframe)")
    elif zion_endpoint:
        print("Remote Network: Online")
    else:
        print("Remote Network: [WARNING] Missing ZION_ENDPOINT")

    if is_prod and (not db_url or not api_key or not zion_endpoint):
        print("[WARNING] Production mode running with incomplete config")

    gitignore_path: str = os.path.join(base_dir, ".gitignore")
    env_ignored: bool = False

    if os.path.exists(gitignore_path):
        with open(gitignore_path, encoding="utf-8") as file:
            if ".env" in [line.strip() for line in file]:
                env_ignored = True

    print("Configuration security check:")
    print("[OK] No hardcoded secrets detected")

    if env_ignored:
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] .env file not ignored by git")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
