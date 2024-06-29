from faker import Faker
from app import app
from models import db, Students, Course
import random

faker = Faker()

# Define custom course descriptions
course_descriptions = [
    "Introduction to basic mathematical concepts.",
    "An overview of fundamental principles of physics.",
    "Exploring the world of computer programming.",
    "Basics of chemistry and chemical reactions.",
    "Understanding the history of the modern world.",
    "Learning the fundamentals of graphic design.",
    "Introduction to psychological theories and practices.",
    "Principles of economics and market dynamics."
]

subject_abbreviations = ["MATH", "PHYS", "COMP", "CHEM", "HIST", "DESG", "PSYC", "ECON"]


print("Seeding started...")
def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()

        for i in range(10):
            student = Students(name=faker.name(), email=faker.email(), age=faker.random_int(min=18, max=25))
            db.session.add(student)
            db.session.commit()
        # student2 = Students(name="Jesus", email="jesus@gmail.com", age=45)
        # db.session.add(student2)
        # db.session.commit()

        for i in range(8):
            description = random.choice(course_descriptions)
            subject=random.choice(subject_abbreviations)
            course_code=faker.random_int(min=100, max=900)
            code = f'{subject} {course_code}'

            course = Course(name=subject, code=code, description=description ,student_id=faker.random_int(min=1, max=10))
            db.session.add(course)
            db.session.commit()

        # course1 = Course(name="Maths", code="MATH 100", description="Introduction to maths", student_id=student2.id)
        # db.session.add(course1)
        # db.session.commit()

seed_data()
print("Seeding completed!")

