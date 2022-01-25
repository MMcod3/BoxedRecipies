import os
from flask import (
    Flask, render_template, url_for,
    redirect, request, flash, session)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def recipes():
    return render_template("recipes.html", page_title="Recipes")


#
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if user already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("User already registered. Please log in!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # new user placed into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("You have successfully registered!")
    return render_template("register.html", page_title="Register")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checking if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # checking user input  matches 
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html", page_title="login")


@app.route("/logout")
def logout():
    # user deleted from session cookie
    flash("Log out successful")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
