import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import *

app = Flask(__name__)
app.config.from_object(Config)
app.debug = True
db = SQLAlchemy()
db.init_app(app)

# db.create_all()

c1 = ('Software Engineering', 1166)
c2 = ('Art History', 1010)
c3 = ('Mathemetical Logic ', 1017)
c4 = ('Theory of Programming ', 1024)
c5 = ('Calc 3', 1012)
courses = [c1,c2,c3,c4,c5]

@app.route("/")
def index():
    course_form = NewCourseForm()
    if course_form.validate_on_submit():
        course_class_id = course_form.class_id.data
        course_course_name = course_form.course_name.data
        course_course_num = course_form.course_num.data
        return redirect(url_for('add_course',
        course_class_id = course_class_id,
        course_num = course_num, course_name = course_name))
    # courses = Course.query.all()
    return render_template('index.html', course_form = course_form, courses = courses)

    # return render_template("index.html", courses = courses)

@app.route("/add_course", methods = ["post"])
def add_flight():
    course_id = request.form.get("course_id")
    course_number = request.form.get("course_number")
    course_title = request.form.get("course_title")
    course = Course(course_id = course_id, course_number=course_number, course_title=course_title)

    db.session.add(flight)
    db.session.commit()
    courses = Course.query.all()
    return render_template('add_flight.html', courses = courses, form=form)

def main():
    if (len(sys.argv)==2):
        print(sys.argv)
        if sys.argv[1] == 'createdb':
            db.create_all()
    else:
        print("Run app using 'flask run'")
        print("To create a database use 'python app.py createdb'")

if __name__ == "__main__":
    with app.app_context():
        main()