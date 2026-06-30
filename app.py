"""

College Attendance Management Portal (CAMP)
Version : 0.2
Developer : Saurabh Mishra
Framework : Flask

"""

from app.services.student_service import (
    get_all_students,
    insert_student
)

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)
from database.database import check_admin_login

#
# Create Flask Application
#

app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="app/static"
)
app.secret_key = "camp_secret_key_2026"

#
# Dashboard (Home Page)
#


@app.route("/")
def dashboard():

    if not session.get("logged_in"):

        return redirect(url_for("login"))

    return render_template(
        "dashboard/dashboard.html",
        active_page="dashboard",
        page_title="Dashboard"
    )


#
# Authentication
#

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        admin = check_admin_login(email, password)

        if admin:

            session["logged_in"] = True
            session["admin_email"] = admin["email"]
            session["admin_name"] = admin["name"]

            return redirect(url_for("dashboard"))

        return render_template(
            "auth/login.html",
            error="Invalid Email or Password"
        )

    return render_template("auth/login.html")


#
# Student Registration
#

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        roll_number = request.form.get("roll_number")
        branch = request.form.get("branch")
        year = request.form.get("year")
        section = request.form.get("section")
        email = request.form.get("email")
        phone = request.form.get("phone")

        insert_student(
            name,
            roll_number,
            branch,
            year,
            section,
            email,
            phone
        )

        return redirect(url_for("students"))

    return render_template(
        "student/register.html",
        active_page="students",
        page_title="Register Student"
    )


#
# Student List
#

@app.route("/students")
def students():

    students = get_all_students()

    return render_template(
        "student/students.html",
        students=students,
        active_page="students",
        page_title="Students"
    )


#
# Attendance
#

@app.route("/attendance")
def attendance():

    return render_template(
        "attendance/attendance.html",
        active_page="attendance",
        page_title="Attendance"
    )


#
# Reports
#

@app.route("/reports")
def reports():

    return render_template(
        "reports/reports.html",
        active_page="reports",
        page_title="Reports"
    )


#
# Settings
#

@app.route("/settings")
def settings():

    return render_template(
        "settings/settings.html",
        active_page="settings",
        page_title="Settings"
    )


#
# QR Verification
#

@app.route("/qr")
def qr():

    return render_template(
        "qr/qr.html",
        active_page="qr",
        page_title="QR Verification"
    )


#
# Logout
#

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


#
# Run Application
#

if __name__ == "__main__":
    app.run(debug=True)
