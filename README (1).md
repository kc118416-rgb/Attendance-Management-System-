# 📋 Attendance Management System

A simple command-line based **Attendance Management System** built with Python. It allows you to manage students, mark daily attendance, and view detailed reports — all stored persistently in a local JSON file.

---

## 🚀 Features

- ➕ Add new students
- 🗑️ Remove existing students
- ✅ Mark attendance (Present / Absent) for today's date
- 📅 View attendance records across all dates
- 🔍 Filter attendance by a specific date
- 📊 View attendance summary with percentage per student
- 💾 Data is saved automatically in a JSON file (persists after closing)

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| `json` | Persistent data storage |
| `tabulate` | Clean table display in terminal |
| `datetime` | Auto-capture today's date |
| `os` | File existence check |

---

## 📁 Project Structure

```
attendance-management-system/
│
├── attendance_system.py      # Main Python file
├── attendance_data.json      # Auto-generated data file (created on first run)
└── README.md                 # Project documentation
```

---

## ⚙️ Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/your-username/attendance-management-system.git
cd attendance-management-system
```

**2. Install the required library**
```bash
pip install tabulate
```

**3. Run the program**
```bash
python attendance_system.py
```

---

## 📌 How to Use

When you run the program, a menu appears:

```
=============================
  ATTENDANCE MANAGEMENT SYSTEM
=============================
1. Add Student
2. View All Students
3. Mark Attendance
4. View Attendance (All Dates)
5. View Attendance by Date
6. View Summary
7. Remove Student
8. Exit
-----------------------------
Enter your choice (1-8):
```

- Enter the number for the action you want to perform
- For marking attendance, enter `p` for **Present** and `a` for **Absent**
- All data is automatically saved after every action

---

## 🖥️ Sample Output

**Student List:**
```
+-----+----------------+
|   # | Student Name   |
+=====+================+
|   1 | Ravi           |
+-----+----------------+
|   2 | Priya          |
+-----+----------------+
|   3 | Arjun          |
+-----+----------------+
```

**Attendance Record:**
```
+-----------+--------------+--------------+
| Student   | 2026-06-24   | 2026-06-25   |
+===========+==============+==============+
| Ravi      | Present      | Present      |
+-----------+--------------+--------------+
| Priya     | Absent       | Present      |
+-----------+--------------+--------------+
| Arjun     | Present      | Absent       |
+-----------+--------------+--------------+
```

**Attendance Summary:**
```
+-----------+--------------+-----------+----------+----------------+
| Student   |   Total Days |   Present |   Absent | Attendance %   |
+===========+==============+===========+==========+================+
| Ravi      |            2 |         2 |        0 | 100.0%         |
+-----------+--------------+-----------+----------+----------------+
| Priya     |            2 |         1 |        1 | 50.0%          |
+-----------+--------------+-----------+----------+----------------+
| Arjun     |            2 |         1 |        1 | 50.0%          |
+-----------+--------------+-----------+----------+----------------+
```

---

## 📦 Requirements

```
tabulate
```

You can also create a `requirements.txt` and install with:
```bash
pip install -r requirements.txt
```

**requirements.txt**
```
tabulate
```

---

## 🙌 Author

Made with ❤️ using Python  
Feel free to fork, star ⭐, and contribute!

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
