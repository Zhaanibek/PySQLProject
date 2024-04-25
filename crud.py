# -*- coding: utf-8 -*-

from models import Grade, User, Student, Class, Score
from sqlalchemy import func, desc


def add_user(session, username, password):
    new_user = User(username=username, password=password)
    session.add(new_user)


def get_user_by_username(session, username):
    return session.query(User).filter_by(username=username).first()


def update_user_password(session, username, new_password):
    user = get_user_by_username(session, username)
    if user:
        user.password = new_password


def delete_user(session, username):
    user = get_user_by_username(session, username)
    if user:
        session.delete(user)


def get_top_3_students(session):
    students_with_avg_score = session.query(Student, func.avg(Score.value).label('avg_score')) \
                                    .join(Student.scores) \
                                    .group_by(Student) \
                                    .all()

    sorted_students = sorted(students_with_avg_score, key=lambda x: x[1], reverse=True)

    top_3_students = sorted_students[:3]

    return top_3_students


def add_grade(session, username, subject, value):
    user = get_user_by_username(session, username)
    if user:
        new_grade = Grade(subject=subject, value=value, user_id=user.id)
        session.add(new_grade)
    else:
        print("Пользователь не найден.")


def get_user_grades(session, username):
    user = get_user_by_username(session, username)
    if user:
        return user.grades
    else:
        print("Пользователь не найден.")


def calculate_average_grades(grades):
    if grades:
        total = sum(grade.value for grade in grades)
        return total / len(grades)
    else:
        return 0


def get_top_students(session, limit=3):
    students = session.query(User).all()
    students.sort(key=lambda x: calculate_average_grades(x.grades), reverse=True)
    return students[:limit]