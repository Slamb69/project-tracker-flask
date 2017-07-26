"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    # return "{acct} is the GitHub account for {first} {last}".format(
    #     acct=github, first=first, last=last)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)

    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching a student."""

    return render_template('student_search.html')


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    github = request.form.get("github")

    hackbright.make_new_student(first_name, last_name, github)

    return render_template("student_added.html",
                           first=first_name,
                           last=last_name,
                           github=github)


@app.route("/student-add", methods=['GET'])
def show_student_add_page():
    """Displays the add student page"""

    return render_template("add_student.html")


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
