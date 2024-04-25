from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base, engine


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    class_id = Column(Integer, ForeignKey('classes.id'))
    class_obj = relationship("Class", back_populates="students")
    grades = relationship("Grade", back_populates="student")
    scores = relationship("Score", back_populates="student")

    def __repr__(self):
        return f"<Student(name='{self.name}')>"


class Score(Base):
    __tablename__ = 'scores'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    value = Column(Float)

    student = relationship("Student", back_populates="scores")


class Class(Base):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)
    average_score = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="classes")
    students = relationship("Student", back_populates="class_obj")


class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)
    value = Column(Integer)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship("Student", back_populates="grades")


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String, unique=True)
    classes = relationship("Class", back_populates="user")

    def __repr__(self):
        return f"username = {self.username}, password = {self.password}"


Base.metadata.create_all(engine)
