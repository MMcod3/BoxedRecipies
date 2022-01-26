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
@app.route("/all_recipes")
def all_recipes():
    recipes = list(mongo.db.recipies.find())
    user = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template(
        "recipes.html", page_title="Recipes", recipes=recipes, user=user )


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "title": request.form.get("title"),
            "cuisine": reuqest.form.get("cuisine_name"),
            "allergens": reuqest.form.getlist("Allergen_name"),
            "ingredients": request.form.getlist("ingredients_name"),
            "instructions": reuqest.form.getlist("instructions_name"),
            "author": session["user"]
        }
        mongo.db.recipies.insert_one(recipe)
        flash("Recipe added!")
        return redirect(url_for("all_recipes"))

    cuisines = list(mongo.db.cuisines.find().sort('cuisine_name', 1))
    ingredients = list(mongo.db.ingredients.find().sort('ingredient_name', 1))
    allergens = list(mongo.db.allergens.find().sort('Allergen_name', 1))
    user = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template(
            "add_recipe.html", page_title="Share Your Recipe",
            user=user, cuisines=cuisines, ingredients=ingredients, allergens=allergens)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipies.find({"$text": {"$search": query}}))
    return render_template(
        "recipes.html", page_title="Recipes", recipes=recipes)


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


@app.route('/this_recipe/<recipe_id>/')
def recipe(recipe_id):
    this_recipe = mongo.db.recipies.find_one({'_id': ObjectId(recipe_id)})
    recipe_id = str(this_recipe['_id'])
    allergens = list(mongo.db.allergens.find())
    return render_template('this_recipe.html', recipe=this_recipe, allergens=allergens, recipe_id=recipe_id)


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipies.remove({'_id': ObjectId(recipe_id)})
    flash('Recipe has been deleted')
    return redirect(url_for('all_recipes'))


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "title": request.form.get("title"),
            "allergens": reuqest.form.getlist("Allergen_name"),
            "ingredients": request.form.getlist("ingredients_name"),
            "instructions": reuqest.form.getlist("instructions_name"),
            "author": session["user"]
        }
        mongo.db.recipies.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Edited!")
        return redirect(url_for("all_recipes"))    


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=False)




