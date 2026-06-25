# falsk creates our web app
# render_template -> displays html pages
from flask import Flask, render_template

# it will create our web application
app = Flask(__name__)

# when someone visit 
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
