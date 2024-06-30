from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()   # Initialize the SQLAlchemy object

            # b) one-to-one relationship between user and profile
class User(db.model, SerializerMixin):
    __tablename__ = 'users_table'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    profile = db.Relationship('Profile', backref='user', lazy=True)

class Profile(db.Model, SerializerMixin):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)
    profile_pic = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.String(200), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users_table.id'), nullable=False)

        # c) Many to many Relationships

class Students(db.Model, SerializerMixin):
    __tablename__ = 'students_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False)


class Course(db.Model, SerializerMixin):
    __tablename__ = 'course_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(200), nullable=False)

class Enrollment(db.Model, SerializerMixin):
    __tablename__ = "enrollment_table"
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primaryKey=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primaryKey=True)

    course = db.relationship('Course', backref='enrollments', lazy=True)
    student = db.relationship('Students', backref='enrollments' , lazy=True)