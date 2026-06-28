"""

College Attendance Management Portal (CAMP)
Version : 0.2
Developer : Saurabh Mishra
Framework : Flask

"""

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

    return render_template("dashboard/dashboard.html")


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

@app.route("/register")
def register():
    return render_template("student/register.html")


#
# Student List
#

@app.route("/students")
def students():
    return render_template("student/students.html")


#
# Attendance
#

@app.route("/attendance")
def attendance():
    return render_template("attendance/attendance.html")


#
# Reports
#

@app.route("/reports")
def reports():
    return render_template("reports/reports.html")


#
# Settings
#

@app.route("/settings")
def settings():
    return render_template("settings/settings.html")


#
# QR Verification
#

@app.route("/qr")
def qr():
    return "<h2>QR Verification Module - Coming Soon</h2>"


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
