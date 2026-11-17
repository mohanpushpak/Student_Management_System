from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from fastapi.responses import RedirectResponse
from enum import Enum
import sqlite3

# Database connection
def get_connection():
    connection = sqlite3.connect("students.db")
    return connection

# Create table
def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    q = """
    CREATE TABLE IF NOT EXISTS Students(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Age INTEGER,
        Gender TEXT,
        Marks INTEGER,
        Course TEXT,
        Image TEXT,
        Status INTEGER
    )
    """

    cursor.execute(q)
    connection.commit()
    connection.close()


create_table()


# Templates
templates = Jinja2Templates(directory="templates")

app = FastAPI()


# Course Enum
class Course(str, Enum):
    python = "python"
    java = "java"
    mern = "mern"


# Student model
class Student(BaseModel):
    name: str = Field(max_length=20, min_length=3)
    age: int = Field(le=24, ge=18)
    gender: str
    marks: int = Field(le=100, ge=0)
    course: Course
    image: str
    status: int


# Home page
@app.get("/")
def home(req: Request):

    connection = get_connection()
    cursor = connection.cursor()

    q = "SELECT * FROM Students"
    cursor.execute(q)

    students = cursor.fetchall()

    connection.close()

    return templates.TemplateResponse(
        request=req,
        name="home.html",
        context={"stds": students}
    )


# Display add student form
@app.get("/students/add")
def send_form(req: Request):

    return templates.TemplateResponse(
        request=req,
        name="add_student.html",
        context={}
    )


# Add student
@app.post("/students/add")
def create_std(
    name: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...),
    marks: int = Form(...),
    course: Course = Form(...),
    image: str = Form(...),
    status: int = Form(...)
):

    student = Student(
        name=name,
        age=age,
        gender=gender,
        marks=marks,
        course=course,
        image=image,
        status=status
    )

    values = (
        student.name,
        student.age,
        student.gender,
        student.marks,
        student.course.value,
        student.image,
        student.status
    )

    connection = get_connection()
    cursor = connection.cursor()

    q = """
    INSERT INTO Students
    (name, age, gender, marks, course, image, status)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    cursor.execute(q, values)

    connection.commit()
    connection.close()

    return RedirectResponse(url="/", status_code=303)


# Display single student
@app.get("/students/{std_id}")
def single_std(req: Request, std_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    q = "SELECT * FROM Students WHERE ID = ?"

    cursor.execute(q, (std_id,))
    student = cursor.fetchone()

    connection.close()

    if student is None:
        return {"message": "Student not found"}

    return templates.TemplateResponse(
        request=req,
        name="single-std.html",
        context={"std": student}
    )


# Delete student
@app.post("/students/{std_id}/delete")
def delete_student(std_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    q = "DELETE FROM Students WHERE ID = ?"

    cursor.execute(q, (std_id,))

    connection.commit()
    connection.close()

    return RedirectResponse(url="/", status_code=303)


# Display edit student form
@app.get("/students/update/{std_id}")
def edit_std(req: Request, std_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    q = "SELECT * FROM Students WHERE ID = ?"

    cursor.execute(q, (std_id,))
    student = cursor.fetchone()

    connection.close()

    if student is None:
        return {"message": "Student not found"}

    return templates.TemplateResponse(
        request=req,
        name="edit-student.html",
        context={"std": student}
    )


# Update student
@app.post("/students/update/{std_id}")
def update_std(
    std_id: int,
    name: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...),
    marks: int = Form(...),
    course: Course = Form(...),
    image: str = Form(...),
    status: int = Form(...)
):

    student = Student(
        name=name,
        age=age,
        gender=gender,
        marks=marks,
        course=course,
        image=image,
        status=status
    )

    values = (
        student.name,
        student.age,
        student.gender,
        student.marks,
        student.course.value,
        student.image,
        student.status,
        std_id
    )

    q = """
    UPDATE Students
    SET name=?,
        age=?,
        gender=?,
        marks=?,
        course=?,
        image=?,
        status=?
    WHERE ID=?
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(q, values)

    connection.commit()
    connection.close()

    return RedirectResponse(url="/", status_code=303)
