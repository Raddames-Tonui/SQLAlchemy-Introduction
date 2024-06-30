from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# Initialize the SQLAlchemy object
db = SQLAlchemy()

# Define the Students model
class Students(db.Model, SerializerMixin):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False)

    # Relationship to Course model
    # 'lazy=True' defers the loading of related Course objects until the courses attribute is accessed
    courses = db.relationship('Course', backref='student', lazy=True)

    # Serialization rules to avoid recursion issues
    serialize_rules = ('-courses.student',)

class Course(db.Model, SerializerMixin):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    # Foreign key to reference Students table
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)

    # Serialization rules to avoid recursion issues
    serialize_rules = ('-student.courses',)