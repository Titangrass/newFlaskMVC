from App.database import db

class Student(db.Model):
    studentId = db.Column(db.Integer, nullable=False, primary_key=True)
    student_firstName = db.Column(db.String, nullable=False)
    student_lastName = db.Column(db.String, nullable=False)
    student_faculty = db.Column(db.String, nullable=False)
    student_degree = db.Column(db.String, nullable=False)
    student_courseLevel = db.Column(db.Integer, nullable=False)
    reviews = db.Column(db.String)

    '''
    review: JSON.stringify([{
        likes: Integer,
        dislikes: Integer
    }])
    '''

    array_of_objects = request.form['array_of_objects']
    
    def __init__(self, student_firstName, student_lastName, student_faculty, student_degree, student_courseLevel, reviews):
        self.student_firstName = student_firstName
        self.student_lastName = student_lastName
        self.student_faculty = student_faculty
        self.student_degree = student_degree
        self.student_courseLevel = student_courseLevel
        self.reviews = reviews
    

    def toJSON(self):
        return{
            'student_firstName' = self.student_firstName,
            'student_lastName' = self.student_lastName
        }



    def rate_review(self):
        if like in self.review:
            like+= 1
        else:
            dislike+= 1


