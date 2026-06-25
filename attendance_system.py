import json
import os
from datetime import date
from tabulate import tabulate

DATA_FILE = "attendance_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"students": [], "attendance": {}}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_student(data):
    name = input("Enter student name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return
    if name in data["students"]:
        print(f"Student '{name}' already exists.")
        return
    data["students"].append(name)
    save_data(data)
    print(f"Student '{name}' added successfully.")

def mark_attendance(data):
    if not data["students"]:
        print("No students found. Please add students first.")
        return

    today = str(date.today())

    if today in data["attendance"]:
        print(f"Attendance already marked for {today}.")
        overwrite = input("Do you want to overwrite? (yes/no): ").strip().lower()
        if overwrite != "yes":
            return

    data["attendance"][today] = {}

    print(f"\nMarking attendance for {today}")
    print("Enter 'p' for Present, 'a' for Absent\n")

    for student in data["students"]:
        while True:
            status = input(f"{student}: ").strip().lower()
            if status in ["p", "a"]:
                data["attendance"][today][student] = "Present" if status == "p" else "Absent"
                break
            else:
                print("Invalid input. Enter 'p' or 'a'.")

    save_data(data)
    print(f"\nAttendance for {today} saved successfully.")

def view_attendance(data):
    if not data["attendance"]:
        print("No attendance records found.")
        return

    dates = sorted(data["attendance"].keys())
    students = data["students"]

    headers = ["Student"] + dates
    rows = []

    for student in students:
        row = [student]
        for d in dates:
            row.append(data["attendance"][d].get(student, "-"))
        rows.append(row)

    print("\n--- Attendance Record ---")
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def view_summary(data):
    if not data["attendance"] or not data["students"]:
        print("No data available.")
        return

    total_days = len(data["attendance"])
    rows = []

    for student in data["students"]:
        present = sum(
            1 for d in data["attendance"]
            if data["attendance"][d].get(student) == "Present"
        )
        absent = total_days - present
        percentage = (present / total_days * 100) if total_days > 0 else 0
        rows.append([student, total_days, present, absent, f"{percentage:.1f}%"])

    headers = ["Student", "Total Days", "Present", "Absent", "Attendance %"]
    print("\n--- Attendance Summary ---")
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def view_students(data):
    if not data["students"]:
        print("No students found.")
        return

    rows = [[i + 1, name] for i, name in enumerate(data["students"])]
    print("\n--- Student List ---")
    print(tabulate(rows, headers=["#", "Student Name"], tablefmt="grid"))

def remove_student(data):
    view_students(data)
    if not data["students"]:
        return

    name = input("Enter student name to remove: ").strip()
    if name not in data["students"]:
        print(f"Student '{name}' not found.")
        return

    data["students"].remove(name)

    for d in data["attendance"]:
        data["attendance"][d].pop(name, None)

    save_data(data)
    print(f"Student '{name}' removed successfully.")

def view_by_date(data):
    if not data["attendance"]:
        print("No attendance records found.")
        return

    print("\nAvailable dates:")
    for i, d in enumerate(sorted(data["attendance"].keys()), 1):
        print(f"  {i}. {d}")

    chosen = input("\nEnter date (YYYY-MM-DD): ").strip()
    if chosen not in data["attendance"]:
        print("No record found for this date.")
        return

    rows = [[s, data["attendance"][chosen].get(s, "-")] for s in data["students"]]
    print(f"\n--- Attendance on {chosen} ---")
    print(tabulate(rows, headers=["Student", "Status"], tablefmt="grid"))

def main():
    data = load_data()

    while True:
        print("\n=============================")
        print("  ATTENDANCE MANAGEMENT SYSTEM")
        print("=============================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Mark Attendance")
        print("4. View Attendance (All Dates)")
        print("5. View Attendance by Date")
        print("6. View Summary")
        print("7. Remove Student")
        print("8. Exit")
        print("-----------------------------")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            mark_attendance(data)
        elif choice == "4":
            view_attendance(data)
        elif choice == "5":
            view_by_date(data)
        elif choice == "6":
            view_summary(data)
        elif choice == "7":
            remove_student(data)
        elif choice == "8":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
