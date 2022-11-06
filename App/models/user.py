from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    firstName = db.Column(db.String) 
    lastName = db.Column(db.String) 
    jobTitle = db.Column(db.String(200))
    reviews = db.relationship('Review', backref=db.backref('user', lazy='joined'))
   
    

    def __init__(self, username, password, firstName, lastName, jobTitle):
        self.username = username
        self.set_password(password)
        self.firstName = firstName
        self.lastName = lastName
        self.jobTitle = jobTitle


    def __repr__(self):
        return f'<User {self.id} {self.username} {self.firstName} {self.lastName} {self.jobTitle}>'

    def toJSON(self):
        return{
            'id': self.id,
            'username': self.username,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'jobTitle': self.jobTitle
            
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
