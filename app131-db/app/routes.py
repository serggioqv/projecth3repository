from app import myapp_obj
from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm
from app.models import recipe
from app.models import user
from app import db
# from <X> import <Y>

#route to display home with all recipes
@myapp_obj.route("/")
def main():
    name = "Recipes"
    #object to retrieve the information from db
    recipe_list = recipe.query.all()
    return render_template("recipes.html", name=name,recipe_list=recipe_list)

#route to retrieve the /recipe/id when loged in (login required)
@myapp_obj.route("/recipe/<int:id>")
@login_required
def view_recipe(id):
    # fetch the recipe by ID
    recipe_item = recipe.query.get(id)
    return render_template("recipe_detail.html", recipe=recipe_item)

#route to delete a selected recipe using its ID (login required)
@myapp_obj.route("/recipe/<int:id>/delete", methods=['GET','POST'])
@login_required
def delete_recipe(id):
    #retrieve recipe by ID
    recipe_item = recipe.query.get(id)
    if recipe_item is None:
        flash("not found")
        return redirect(url_for("main"))
    #delete and commit
    db.session.delete(recipe_item)
    db.session.commit()
    flash("Recipe deleted successfully.")
    return redirect(url_for("main"))

#route to handle login to the web application /login
@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    #redirecting logged in users
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = LoginForm()

    if form.validate_on_submit():
        user_obj=user.query.filter_by(username=form.username.data).first()
        if user_obj and user_obj.check_password(form.password.data):
            login_user(user_obj)
            flash("logged in")
            return redirect(url_for("main"))
        else:
            flash("Invalid username/password")
        return render_template("login.html",form=form)
    else:
        print("MOOOO MOOO")
    return render_template("login.html", form=form)

#endpoint to logout from session using /logout
@myapp_obj.route("/logout")
@login_required
def logout():
    logout_user()
    flash("logged out")
    return redirect(url_for("main"))

#route to add a new recipe using GET and POST' (login required)
@myapp_obj.route("/recipe/new", methods=['GET', 'POST'])
@login_required
def new_recipe():
    if request.method == "POST":
        #ensure user is authenticated
        if not current_user.is_authenticated:
            flash("Please log in")
            return redirect(url_for("login"))
        #retrieve form data
        title = request.form["title"]
        description = request.form["description"]
        ingredients = request.form["ingredients"]
        instructions = request.form["instructions"]
        #create and save recipe
        new_recipe=recipe(title=title,
                          description=description,
                          ingredients=ingredients,
                          instructions=instructions,
                          user_id=current_user.id)
        db.session.add(new_recipe)
        db.session.commit()
        return redirect(url_for("main"))
    return render_template("new_recipe.html")