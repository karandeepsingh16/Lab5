from flask_sqlalchemy import SQLAlchemy
from app import db
import os, csv, sys

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()



class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key = True)
    course_number = db.Column(db.String, nullable = False)
    course_title = db.Column(db.String, nullable = False)
    student = db.relationship("Student", backref="Courses", lazy=True)


    def add_student(self, name, grade):
        # Notice that we set the foreign key for the passenger class.
        new_Student = RegisteredStudent(name=name, grade = grade, course_id=self.id )
        db.session.add(new_Student)
        db.session.commit()

        
class RegisteredStudent(db.Model):
    __tablename__ = "registeredstudents"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    grade = db.Column(db.Integer, nullable = False)
    course_id = db.Column(db.Integer, db.ForeignKey('Courses.id'))

