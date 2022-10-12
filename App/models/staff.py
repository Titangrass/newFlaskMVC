from App.database import db

class Staff(db.Model):
    staff_firstName = db.Column(db.String, nullable=False) 
    staff_lastName = db.Column(db.String, nullable=False) 
    staff_jobTitle = db.Column(db.String)
    staff_reviews = db.Column(db.String, db.ForeignKey('Review.comment'))
    
    def __init__(self, staff_firstName, staff_lastName):
        self.staff_firstName = staff_firstName
        self.staff_lastName = staff_lastName

    def toJSON(self):
        return{
            'staff_firstName' = staff_firstName
            'staff_lastName' = staff_lastName
            'staff_jobTitle' = staff_jobTitle
            'staff_reviews' = staff_reviews
        }


