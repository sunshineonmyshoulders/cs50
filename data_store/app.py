from flask import Flask, render_template, request, session
from flask_session import *

app = Flask(__name__)

session = Session()
def create_app():
	app = Flask(__name__)
	sess.init_app(app)
	return app


"""
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)"""

notes = []

@app.route("/", methods=["GET", "POST"])
def index():
	session["notes"] = []
	if request.method == "POST":
		note = request.form.get("note")
		session["notes"].append(note)

	return render_template("index.html", notes=session["notes"]) 
