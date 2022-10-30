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
            like += 1
        else:
            dislike += 1
  
"""
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


    def getKarmaScore(self):
        numLikes = 0
        numDislikes =0
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