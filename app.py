"""

College Attendance Management Portal (CAMP)
Version : 0.2
Developer : Saurabh Mishra
Framework : Flask

"""

from flask import Flask, render_template

#
# Create Flask Application
#

app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="app/static"
)

#
# Dashboard (Home Page)
#


@app.route("/")
def dashboard():
    return render_template("dashboard/dashboard.html")


#
# Authentication
#

@app.route("/login")
def login():
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
    return "<h2>Logout Module - Coming Soon</h2>"


#
# Run Application
#

if __name__ == "__main__":
    app.run(debug=True)
