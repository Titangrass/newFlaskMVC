from App.models import Student
from App.database import db
from App.config import config
import requests
import json


def add_Student(studentId, student_firstName, student_lastName, student_faculty, student_degree, student_courseLevel, reviews):
    new_student = Student(studentId=studentId, student_firstName=student_firstName, student_lastName=student_lastName, student_faculty=student_faculty, student_degree=student_degree, student_courseLevel=student_courseLevel, reviews=reviews)
    db.session.add(new_student)
    db.session.commit()
    return new_review

def get_student(studentId):
    return User.query.get(studentId)

def update_student(studentId, student_firstName, student_lastName, student_faculty, student_degree, student_courseLevel, reviews):
    student = get_student(studentId):
    if student:
        student.studentId = studentId
        student.student_firstName = student_firstName
        student.student_lastName = student_lastName
        student.student_faculty = student_faculty
        student.student_degree = student_degree
        student.reviews = reviews
        db.session.add(student)
        return db.session.commit()
    return None




