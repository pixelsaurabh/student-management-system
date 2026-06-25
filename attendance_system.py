import csv
import os
from datetime import datetime


def mark_attendance(name):
    file_path = "attendance/attendance.csv"

    # Create file and header if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Date", "Time"])

    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    already_marked = False

    with open(file_path, "r", newline="") as f:
        reader = csv.reader(f)

        for row in reader:
            if len(row) >= 2:
                if row[0] == name and row[1] == today:
                    already_marked = True
                    break

    if not already_marked:
        with open(file_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, today, current_time])

        print(f"Attendance marked for {name}")

    else:
        print(f"{name} already marked today")
