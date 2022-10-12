from App.database import db

class Student(db.Model):
    staff_firstName = db.Column(db.String, nullable=False) 
    staff_lastName = db.Column(db.String, nullable=False) 
    staff_jobTitle = db.Column(db.String)
    staff_reviews = db.Column(db.String)

    studentId = db.Column(db.Integer, nullable=False, primary_key=True)
    student_firstName = db.Column(db.String, nullable=False)
    student_lastName = db.Column(db.String, nullable=False)
    student_faculty = db.Column(db.String, nullable=False)
    student_degree = db.Column(db.String, nullable=False)
    student_courseLevel = db.Column(db.Integer, nullable=False)
    reviews = db.Column(db.String)
    
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


