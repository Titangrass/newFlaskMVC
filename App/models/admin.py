from App.database import db

class User(db.Model):
    admin_name = db.Column(db.String, primary_key=True)
    email = db.Column(db.String, nullable=False)


    def __init__(self, admin_name):
        self.admin_name = admin_name

    def toJSON(self):
        return{
            'id': self.id,
        }

