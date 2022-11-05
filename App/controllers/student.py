from App.models import Student
from App.database import db
from App.config import config
import requests
import json


def add_student(firstName, lastName, faculty, degree, courselevel):
    newstudent = Student(firstName=firstName, lastName=lastName, faculty=faculty, degree=degree, courseLevel=courseLevel)
    db.session.add(newstudent)
    db.session.commit()
    return newstudent

def search_student(studentId):
    return Student.query.get(studentId)

def update_student(studentId, data):
    student = search_student(studentId)
    if student:
        if data["firstName"]:
            student.firstName = data['firstName']
        if data["lastName"]:
            student.lastName = data['lastName']
        if data["faculty"]:
            student.faculty = data['faculty']
        if data["degree"]:
            student.degree = data['degree']
        if data["courseLevel"]:
            student.courseLevel = data['courseLevel']
        db.session.add(student)
        return db.session.commit()
    return None

def getKarmaScore(self):
        numLikes = 0
        numDislikes = 0
        score = 0
        for review in self.reviews:
            if review.like:
                numLikes += 1

            if review.dislike:
                numDislikes +=1
        total = numDislikes + numLikes
        score = (numLikes - numDislikes/total)*100
        return score

"""
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

"""


