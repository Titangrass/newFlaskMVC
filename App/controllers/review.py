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


