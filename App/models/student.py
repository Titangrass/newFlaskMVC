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
    
    def __init__(self, student_firstName, student_lastName):
        self.student_firstName = student_firstName
        self.student_lastName = student_lastName
    

    def toJSON(self):
        return{
            'student_firstName' = student_firstName
            'student_lastName' = student_lastName
        }


