
import csv
from datetime import datetime
from pathlib import Path

# CSV will be saved beside this Python script
PROJECT_DIR = Path(__file__).resolve().parent


def main():
    print("=" * 40)
    print("       SmartAttend-Arduino")
    print("       Attendance Logger")
    print("=" * 40)

    message = input("\nPaste Serial Monitor message: ").strip().upper()

    if message != "YOGI_PRESENT":
        print("Invalid message. Expected: YOGI_PRESENT")
        return

    date_input = input(
        "Enter attendance date (YYYY-MM-DD), "
        "or press Enter for today: "
    ).strip()

    try:
        if date_input:
            attendance_date = datetime.strptime(
                date_input, "%Y-%m-%d"
            ).date()
        else:
            attendance_date = datetime.now().date()
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")
        return

    current_time = datetime.now().strftime("%H:%M:%S")
    formatted_date = attendance_date.strftime("%d-%m-%Y")

    # Example: oct11.csv
    filename = attendance_date.strftime("%b%d").lower() + ".csv"
    file_path = PROJECT_DIR / filename

    file_exists = file_path.exists()

    with file_path.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists or file_path.stat().st_size == 0:
            writer.writerow(["Name", "Status", "Date", "Time"])

        writer.writerow([
            "YOGI",
            "Present",
            formatted_date,
            current_time
        ])

    print("\nAttendance recorded successfully!")
    print(f"Name: YOGI")
    print(f"Status: Present")
    print(f"Date: {formatted_date}")
    print(f"Time: {current_time}")
    print(f"Saved to: {file_path}")


if __name__ == "__main__":
    main()
