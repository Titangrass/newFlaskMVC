import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import User
from App.controllers import (
    create_user,
    get_all_users_json,
    authenticate,
    get_user,
    get_user_by_username,
    update_user
)

from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        user = User("allisonHarper127", "allison", "harper", "teacher", "allie127")
        assert user.username == "allisonHarper127"

    # pure function no side effects or integrations called
    def test_toJSON(self):
        user = User("allison", "harper", "teacher", "allie127")
        user_json = user.toJSON()
        self.assertDictEqual(user_json, {"id":None, "username":"allisonHarper127", "staff_firstName":"allison", "staff_lastName":"harper", "staff_jobTitle":"teacher", "password":"allie127"})

    
    def test_hashed_password(self):
        hashed = generate_password_hash(password, method='sha256')
        user = User("allisonHarper127", "allison", "harper", "teacher", "allie127")
        assert user.password != password

    def test_check_password(self):
        password = "allie127"
        user = User("allisonHarper127", "allison", "harper", "teacher", "allie127")
        assert user.check_password(password)

    def test_add_Student(self):
        new_student = Student("David", "Moriarty", "FST", "Computer Science", 3)

    
    def test_create_review(self):
        new_review = review("allisonHarper127", "101")

'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app.config.update({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db(app)
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/test.db')


def test_authenticate():
    user = create_user("bob", "bobpass")
    assert authenticate("bob", "bobpass") != None

class UsersIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        user = create_user("rick", "bobpass")
        assert user.username == "rick"

    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual([{"id":1, "username":"bob"}, {"id":2, "username":"rick"}], users_json)

    # Tests data changes in the database
    def test_update_user(self):
        update_user(1, "ronnie")
        user = get_user(1)
        assert user.username == "ronnie"
