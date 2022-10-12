from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(120), nullable=False)

    username = db.Column(db.String(120), nullable=False)

    staff_firstName = db.Column(db.String, nullable=False) 
    staff_lastName = db.Column(db.String, nullable=False) 
    staff_jobTitle = db.Column(db.String)
    staff_reviews = db.Column(db.String, db.ForeignKey('Review.comment')

    def __init__(self, id, password, staff_firstName, staff_lastName, staff_jobTitle, staff_reviews):
        self.id = id
        self.set_password(password)
        self.staff_firstName = staff_firstName
        self.staff_lastName = staff_lastName
        self.staff_jobTitle = staff_jobTitle
        self.staff_reviews = staff_reviews

    def toJSON(self):
        return{
            'id': self.id,
            'staff_firstName' = self.staff_firstName,
            'staff_lastName' = self.staff_lastName,
            'staff_jobTitle' = self.staff_jobTitle,
            'staff_reviews' = self.staff_reviews
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

