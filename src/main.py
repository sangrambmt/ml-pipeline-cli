from dotenv import load_dotenv
import os


def main() -> None:
    load_dotenv()

    app_env = os.getenv("APP_ENV", "dev")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    input_dir = os.getenv("INPUT_DIR", "data/raw")
    output_dir = os.getenv("OUTPUT_DIR", "data/processed")

    print("Project is running")
    print(f"APP_ENV: {app_env}")
    print(f"LOG_LEVEL: {log_level}")
    print(f"INPUT_DIR: {input_dir}")
    print(f"OUTPUT_DIR: {output_dir}")


if __name__ == "__main__":
    main()