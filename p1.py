# from fastapi import FastAPI, Request, Form 

# from fastapi.templating import Jinja2Templates

# from pydantic import BaseModel, Field

# import sqlite3

# def get_connection():
#     connection=sqlite3.connect(
#         "students.db"
#     )
#     return connection
# get_connection()

# def create_table():
#     connection=get_connection()
#     cursor=connection.cursor()
#     q=""" 
#     CREATE TABLE IF NOT EXISTS STUDENT(
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     NAME TEXT NOT NULL,
#     AGE INTEGER,
#     GENDER TEXT,
#     MARKS INTEGER,
#     COURSE TEXT,
#     IMAGE TEXT,
#     STATUS INTEGER
#     )
#     """
#     cursor.execute(q)
#     connection.commit()
#     connection.close()
# create_table()

# templates=Jinja2Templates(
#     directory="templates-1"
# )

# class student(BaseModel):
#     name: str = Field(min_length=3)
#     age: int = Field(gt=0)
#     gender: str
#     marks: int = Field(ge=0)
#     course: str
#     image: str
#     status: int = Field(ge=0, le=1)

# app=FastAPI()

# @app.get("/")
# def home(req:Request):
#     return templates.TemplateResponse(
#         request=req,
#         name="home.html",
#         context={}
#     )


# @app.get("/students/add")
# def send_std_form(req: Request):
#     return templates.TemplateResponse(
#         request=req,
#         name="add-std.html",
#         context={}
#     )


# @app.post("/students/add")
# def create_stu(name=Form(),age=Form(),gender=Form(),marks=Form(),course=Form(),image=Form(),status=Form()):
#     
#     s=student(name=name,age=age,gender=gender,marks=marks,course=course,image=image,status=status)
# 
#     values=(s.name,s.age,s.gender,s.marks,s.course,s.image,s.status)
#     
#     connection=get_connection()
#     cursor= connection.cursor()
#     q=""" INSERT INTO STUDENT(name,age,gender,marks,course,image,status) VALUES(?,?,?,?,?,?,?)"""
#     cursor.execute(q, values)
#     connection.commit()
#     connection.close()
#     return{
#         "mes":"student added",
#         "data":s
#     }




# from fastapi import FastAPI, Request, Form 

# from fastapi.templating import Jinja2Templates

# from pydantic import BaseModel, Field


# import sqlite3

# from pydantic import ValidationError
# from fastapi import HTTPException


# def get_connection():
#     connection=sqlite3.connect(
#         "students.db"
#     )
#     return connection
# get_connection()

# def create_table():
#     connection=get_connection()
#     cursor=connection.cursor()
#     q=""" 
#     CREATE TABLE IF NOT EXISTS STUDENT(
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     NAME TEXT NOT NULL,
#     AGE INTEGER,
#     GENDER TEXT,
#     MARKS INTEGER,
#     COURSE TEXT,
#     IMAGE TEXT,
#     STATUS INTEGER
#     )
#     """
#     cursor.execute(q)
#     connection.commit()
#     connection.close()
# create_table()

# templates=Jinja2Templates(
#     directory="templates-1"
# )

# class Student(BaseModel):
#     name: str = Field(min_length=3, max_length=25)
#     age: int = Field(gt=0,lt=100)
#     gender: str
#     marks: int = Field(ge=0,lt=100)
#     course: str =Field(min_length=1,max_length=50)
#     image: str
#     status: int = Field(ge=0, le=1)

# app=FastAPI()

# @app.get("/")
# def home(req:Request):
#     return templates.TemplateResponse(
#         request=req,
#         name="home.html",
#         context={}
#     )


# @app.get("/students/add")
# def send_std_form(req:Request):
#     return templates.TemplateResponse(
#         request=req,
#         name="add-std.html",
#         context={}
#     )


# @app.post("/students/add")
# def create_stu(name=Form(),age=Form(),gender=Form(),marks=Form(),course=Form(),image=Form(),status=Form()):
    
#     try:
#         s = Student(name=name,age=age,gender=gender,marks=marks,course=course,image=image,status=status)
    
#     except ValidationError as e:
#         raise HTTPException(status_code=422, detail=e.errors())
    
#     values=(s.name,s.age,s.gender,s.marks,s.course,s.image,s.status)
    
#     connection=get_connection()
#     cursor= connection.cursor()
#     q=""" INSERT INTO STUDENT(name,age,gender,marks,course,image,status) VALUES(?,?,?,?,?,?,?)"""
#     cursor.execute(q, values)
#     connection.commit()
#     connection.close()
#     return{
#         "mes":"student added",
#         "data":s
#     }




from fastapi import FastAPI, Request, Form, status
import fastapi 

from fastapi.templating import Jinja2Templates

from pydantic import BaseModel, Field

from fastapi.responses import RedirectResponse

import sqlite3

from pydantic import ValidationError
from fastapi import HTTPException

templates=Jinja2Templates(
    directory="templates-1"
)

def get_connection():
    connection=sqlite3.connect(
        "students.db"
    )
    return connection
get_connection()

def create_table():
    connection=get_connection()
    cursor=connection.cursor()
    q=""" 
    CREATE TABLE IF NOT EXISTS STUDENT(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    AGE INTEGER,
    GENDER TEXT,
    MARKS INTEGER,
    COURSE TEXT,
    IMAGE TEXT,
    STATUS INTEGER
    )
    """
    cursor.execute(q)
    connection.commit()
    connection.close()
create_table()


class Student(BaseModel):
    name: str = Field(min_length=3, max_length=25)
    age: int = Field(gt=0,lt=100)
    gender: str
    marks: int = Field(ge=0,lt=100)
    course: str =Field(min_length=1,max_length=50)
    image: str
    status: int = Field(ge=0, le=1)

app=FastAPI()

@app.get("/")
def home(req:Request):
    connection=get_connection()
    cursor=connection.cursor()
    q="select * from student"
    cursor.execute(q)
    students=cursor.fetchall()
    # print(students)
    connection.close()
    return templates.TemplateResponse(
        request=req,
        name="home.html",
        context={
            "std":students    
        }
    )

@app.get("/students/add")
def send_std_form(req:Request):
    return templates.TemplateResponse(
        request=req,
        name="add-std.html",
        context={}
    )


@app.post("/students/add")
def create_stu(name=Form(),age=Form(),gender=Form(),marks=Form(),course=Form(),image=Form(),status=Form()):
    
    try:
        s = Student(name=name,age=age,gender=gender,marks=marks,course=course,image=image,status=status)
    
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    
    values=(s.name,s.age,s.gender,s.marks,s.course,s.image,s.status)
    
    connection=get_connection()
    cursor= connection.cursor()
    q=""" INSERT INTO STUDENT(name,age,gender,marks,course,image,status) VALUES(?,?,?,?,?,?,?)"""
    cursor.execute(q, values)
    connection.commit()
    connection.close()
    return RedirectResponse(url="/", status_code=303)


@app.get("/students/{std_id}")
def single_stu_details(req:Request, std_id:int):
    connection=get_connection()
    cursor=connection.cursor()
    q="select * from student where id=?"
    cursor.execute(q, (std_id,))
    students=cursor.fetchone()
    # print(students)
    connection.close()
    return templates.TemplateResponse(
        request=req,
        name="single_std.html",
        context={
            "std":students    
        }
    )

@app.post("/std/delete/{std_id}")
def delete_std(std_id:int):
    connection=get_connection()
    cursor=connection.cursor()
    q="delete  from student where id=?"
    cursor.execute(q, (std_id,))
    connection.commit()
    connection.close()
    return RedirectResponse(url="/", status_code=303)


@app.get("/students/edit/{std_id}")
def edit_std(req:Request, std_id:int):
    connection=get_connection()
    cursor=connection.cursor()
    q="select *  from student where id=?"
    cursor.execute(q, (std_id,))
    Student=cursor.fetchone()
    connection.close()
    # print(Student)
    if Student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return templates.TemplateResponse(
        request=req,
        name="update.html",
        context={
            "std":Student
        }
    )


@app.post("/students/edit/{std_id}")
def update_stu(std_id=int,name=Form(),age=Form(),gender=Form(),marks=Form(),course=Form(),image=Form(),status=Form()):
    
    std_obj=Student(name=name,age=age,gender=gender,marks=marks,course=course,image=image,status=status)

    values=(std_obj.name,std_obj.age,std_obj.gender,std_obj.marks,std_obj.course,std_obj.image,std_obj.status,std_id)

    connection=get_connection()
    cursor=connection.cursor()
    q=""" update student set name=?, age=?, gender=?, marks=?, course=?, image=?, status=?  where id=?  """
    cursor.execute(q,values)
    connection.commit()
    connection.close()
    return RedirectResponse(url="/", status_code=fastapi.status.HTTP_303_SEE_OTHER)









