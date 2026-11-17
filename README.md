# 🎓 Student Management System

A web-based Student Management System built with **Python FastAPI and SQLite** to simplify student registration and academic record management.

## 📌 Project Overview

The Student Management System provides a centralized platform to manage student information efficiently. It allows administrators to add new students, view student profiles, update existing records, and delete student details through a user-friendly web interface.

## 🚀 Features

- ➕ Add new student records
- 👨‍🎓 View all registered students
- 🔍 View individual student details
- ✏️ Update student information
- 🗑️ Delete student records
- 📚 Manage multiple courses
- 📊 Store and manage academic marks
- 🖼️ Maintain student profile images
- ✅ Validate student information

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | Web framework |
| SQLite | Database management |
| Pydantic | Data validation |
| Jinja2 | HTML templating |
| HTML | Web page structure |
| CSS | Styling |
| JavaScript | Frontend functionality |
| Uvicorn | ASGI server |

## 📂 Project Structure

```text
STUDENT_MANAGEMENT_SYSTEM/
│
├── templates/
│   ├── home.html
│   ├── add_student.html
│   ├── single-std.html
│   └── edit-student.html
│
├── app.py
├── students.db
└── README.md
```

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/mohanpushpak/STUDENT_MANAGEMENT_SYSTEM.git
```

**2. Navigate to the project directory**

```bash
cd STUDENT_MANAGEMENT_SYSTEM
```

**3. Install the required packages**

```bash
pip install fastapi uvicorn jinja2 python-multipart
```

**4. Run the application**

```bash
uvicorn app:app --reload
```

*Note: Replace `app` with your Python filename if it is different.*

**5. Open the application**

```text
http://127.0.0.1:8000
```

## 📚 Available Courses

- Python
- Java
- MERN Stack

## 🎯 Project Objective

The primary objective is to reduce manual paperwork, organize student information, improve record management, and provide a simple digital solution for educational institutions.

## 👨‍💻 Developer

**Mohan Pushpak**

GitHub: [@mohanpushpak](https://github.com/mohanpushpak)

---

⭐ If you find this project useful, consider giving it a star!
