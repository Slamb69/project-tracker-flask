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

    # FIX THIS !!!!!!!!!!!!!!!!!!!!
    # if request.method == 'POST':
    #     return redirect('/student-added')

    # return render_template("add_student.html")
    pass



@app.route("/student-added", methods=['POST'])
def student_added_display():
    """Displays a page confirming that a sudent was added."""

    new_student = request.form.get("first_name", "last_name", "github")

    first, last, github = hackbright.make_new_student(new_student[0],
                                                      new_student[1],
                                                      new_student[2])

    return render_template("student_added.html",
                           first=first,
                           last=last,
                           github=github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
