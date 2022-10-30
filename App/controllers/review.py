from App.models import Review
from App.database import db
from App.config import config
import requests
import json


def create_review(reviewId, userId, studentId, comment, like, dislike):
    new_review = Review(reviewId=reviewId, userId=userId, studentId=studentId, comment=comment, like=like, dislike=dislike)
    db.session.add(new_review)
    db.session.commit()
    return new_review

def rate_review(self):

"""
def log_review(userId, studentId):
    student = Student.query.get(studentId=studentId)
    if student:
             review = Review(userId=userId, studentId=studentId, comment=comment, like=like)
             db.session.add(review)
             db.session.commit()
             return review
    return False
    
def view_student_reviews(studentId): #view all the reviews about a particular student
    return Review.query.filter(studentId=studentId).all()

def view_user_reviews(userId): #a user can view all the reviews made by themselves
    return Review.query.filter(userId=userId).all()

def like_review(reviewId, studentId):
    review = Review.query.filter(reviewId=reviewId, studentId=studentId)
    if review:
        review.like = True
        db.session.add(review)
        db.session.commit()
        return True
    return False

 def dislike_review(reviewId, studentId):
    review = Review.query.filter(reviewId=reviewId, studentId=studentId)
    if review:
        review.dislike = True
        db.session.add(review)
        db.session.commit()
        return True
    return False       

"""       
    


