# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Student, Class, Grade, Score

load_dotenv()

url_str = os.environ.get('url')
engine = create_engine(url_str)
Base.metadata.create_all(engine)

fake = Faker()
#
Session = sessionmaker(bind=engine)
session = Session()
#
# for _ in range(10):
#     username = fake.user_name()
#     password = fake.password(length=12)
#     user = User(username=username, password=password)
#     session.add(user)
#
# for _ in range(5):
#     subject = fake.random_element(["Math", "Physics", "Chemistry", "Biology", "History"])
#     average_score = fake.random_int(min=60, max=100)
#     class_ = Class(subject=subject, average_score=average_score)
#     session.add(class_)
#
# for _ in range(20):
#     name = fake.name()
#     class_id = fake.random_int(min=1, max=5)
#     student = Student(name=name, class_id=class_id)
#     session.add(student)
#
# for _ in range(50):
#     student_id = fake.random_int(min=1, max=10)
#     subject = fake.random_element(["Math", "Physics", "Chemistry", "Biology", "History"])
#     value = fake.random_int(min=60, max=100)
#     grade = Grade(student_id=student_id, subject=subject, value=value)
#     session.add(grade)
#
# for _ in range(100):
#     student_id = fake.random_int(min=1, max=10)
#     value = fake.random_int(min=60, max=100)
#     score = Score(student_id=student_id, value=value)
#     session.add(score)
#
# session.commit()
# session.close()

student = session.query(Student).first()  # Получаем первого студента из базы данных
print(student.name)  # Выводим имя студента
