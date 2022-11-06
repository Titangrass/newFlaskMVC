import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import create_db, get_migrate
from App.main import create_app
from App.controllers import ( 
    
    create_user,
    get_all_users_json,
    get_all_users,
    add_student,
    get_all_students,
    get_all_students_json,
    log_review, 
    view_student_reviews,
    view_user_reviews,
    like_review,
    dislike_review,
       
)

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    create_db(app)
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
@click.argument("firstName", default="Rob")
@click.argument("lastName", default="Smith")
@click.argument("jobTitle", default="Tutor")
def create_user_command(username, password, firstName, lastName, jobTitle):
    user = create_user(username, password, firstName, lastName, jobTitle)
    print(f'{user.username} created!')

# this command will be : flask user create bob bobpass Bob Duncan Lecturer

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

@user_cli.command("user_reviews", help="Shows the reviews written by a user")
def list_user__reviews_command():
    print(get_all_users())
    userId = input('Enter a userId: ')
    print(view_user_reviews(userId))

app.cli.add_command(user_cli) # add the group to the cli

'''
Student Commands
'''
# create a group, it would be the first argument of the comand
# eg : flask student <command>
student_cli = AppGroup('student', help='Student object commands')

# Then define the command and any parameters and annotate it with the group (@)
@student_cli.command("add", help="Adds a student")
@click.argument("firstName", default="Carl")
@click.argument("lastName", default="White")
@click.argument("faculty", default="Food&Agriculture")
@click.argument("degree", default="BscAgribusinessManagement")
@click.argument("status", default="part-time")
@click.argument("courseLevel", default="Year2")
def add_student_command(firstName, lastName, faculty, degree, status, courselevel):
    add_student(firstName, lastName, faculty, degree, status, courselevel)
    print(f'Student {firstName} {lastName} created!')

# this command will be : flask student add John Baptist Science&Technology BscComputerScience full-time Year1

@student_cli.command("list", help="Lists students in the database")
@click.argument("format", default="string")
def list_student_command(format):
    if format == 'string':
        print(get_all_students())
    else:
        print(get_all_students_json())

@student_cli.command("student_reviews", help="Shows the reviews about a particular student")
def list_student_reviews_command():
    print(get_all_students())
    studentId = input('Enter a studentId: ')
    print(view_student_reviews(studentId))

app.cli.add_command(student_cli) # add the group to the cli

'''
Review Commands
'''
# create a group, it would be the first argument of the comand
# eg : flask student <command>
review_cli = AppGroup('review', help='Review object commands')

# Then define the command and any parameters and annotate it with the group (@)
@review_cli.command("log", help="Lets a user log a review about a student")
def log_review_command():
    print(get_all_users())
    userId = input('Enter user Id: ')
    print(get_all_students())
    studentId = input('Enter student Id: ')
    log_review(userId, studentId)
    print("Review logged!")

@review_cli.command("like", help="Lets a user like a review about a student")
def like_review_command():
    print(get_all_users())
    userId = input('Enter user Id: ')
    print(get_all_students())
    studentId = input('Enter student Id: ')
    print(view_student_reviews(studentId))
    reviewId = input('Enter review Id: ')
    like_review(reviewId, userId, studentId)
    print("Review liked!")

@review_cli.command("dislike", help="Lets a user dislike a review about a student")
def dislike_review_command():
    print(get_all_users())
    userId = input('Enter user Id: ')
    print(get_all_students())
    studentId = input('Enter student Id: ')
    print(view_student_reviews(studentId))
    reviewId = input('Enter review Id: ')
    dislike_review(reviewId, userId, studentId)
    print("Review disliked!")

app.cli.add_command(review_cli) # add the group to the cli

'''
Generic Commands
'''

@app.cli.command("init")
def initialize():
    create_db(app)
    print('database intialized')

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)