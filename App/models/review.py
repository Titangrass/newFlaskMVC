from App.database import db

class Review(db.Model):
    reviewId = db.Column(db.Integer, primary_key=True, nullable=False) 
    userId = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    studentId = db.Column(db.Integer, db.ForeignKey('Student.studentId'), nullable=False)
    comment = db.Column(db.String)
    like = db.Column(db.Integer)
    dislike = db.Column(db.Integer, nullable)
    
    def __init__(self, reviewId):
        self.reviewId = reviewId
        self.userId = userId
        self.studentId = studentId
        self.comment = comment
        self.like = like
        self.dislike = dislike
    

    def toJSON(self):
        return{
            'reviewId' = self.reviewId
        }
        



