# from fastapi import FastAPI, Request, Form 

# from fastapi.templating import Jinja2Templates

# from pydantic import BaseModel, Field

# import sqlite3

# from pydantic import ValidationError
# from fastapi import HTTPException


# def get_connection():
#     connection=sqlite3.connect(
#         "p1-students.db"
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


# @app.get("/student/add")
# def send_std_form(req:Request):
#     return templates.TemplateResponse(
#         request=req,
#         name="add-std.html",
#         context={}
#     )


# @app.post("/student/add")
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














