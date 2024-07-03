from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()   # Initialize the SQLAlchemy object

        # a) one to many relationship between students and courses
# Define the Students model
class Students(db.Model, SerializerMixin):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False)

    # Relationship to Course model
    courses = db.relationship('Course', backref='student', lazy=True)     # 'lazy=True' defers the loading of related Course objects until the courses attribute is accessed

    # serialize_rules = ('-courses.student',)     # Serialization rules to avoid recursion issues

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'email': self.email,
            'courses': [course.to_dict() for course in self.courses]
        }
    @validates('email')
    def validate_email(self, key, email):
        if "@" not in email:
            raise ValueError("Invalid email address")
        return email
    
class Course(db.Model, SerializerMixin):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'description': self.description,
            'student_id': self.student_id
        }

    # Foreign key to reference Students table
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)

    # serialize_rules = ('-student.courses',)

