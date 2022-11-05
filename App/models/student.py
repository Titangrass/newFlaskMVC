from App.database import db

class Student(db.Model):
    studentId = db.Column(db.Integer, nullable=False, primary_key=True)
    firstName = db.Column(db.String, nullable=False)
    lastName = db.Column(db.String, nullable=False)
    faculty = db.Column(db.String)
    degree = db.Column(db.String)
    courseLevel = db.Column(db.Integer)
    reviews = db.relationship('Review', backref=db.backref('user', lazy='joined'))
    
    def __init__(self, firstName, lastName, faculty, degree, courseLevel):
        self.firstName = firstName
        self.lastName = lastName
        self.faculty = faculty
        self.degree = degree
        self.courseLevel = courseLevel
    
    def __repr__(self):
        return f'<Student {self.studentId} {self.firstName} {self.lastName} {self.faculty} {self.degree} {self.courseLevel}>'


    def toJSON(self):
        return{
            'studentId'= self.studentId,
            'firstName' = self.firstName,
            'lastName' = self.lastName,
            'faculty' = self.faculty,
            'degree' = self.degree,
            'courseLevel' = self.courseLevel
            'karmaScore' = self.getKarmaScore()
        }

