from app import myapp_obj
from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm
from app.models import recipe
from app.models import user
from app import db
# from <X> import <Y>

'route to display all recipes'
@myapp_obj.route("/")
def main():
    name = "Recipes"
    recipe_list = recipe.query.all()
    return render_template("recipes.html", name=name,recipe_list=recipe_list)
@myapp_obj.route("/recipe/<int:id>")
@login_required
def view_recipe(id):
    # Fetch the recipe by ID
    recipe_item = recipe.query.get(id)
    return render_template("recipe_detail.html", recipe=recipe_item)


@myapp_obj.route("/recipe/<int:id>/delete", methods=['GET','POST'])
@login_required
def delete_recipe(id):
    # Retrieve recipe by ID
    recipe_item = recipe.query.get(id)

    if recipe_item is None:
        flash("Recipe not found.")
        return redirect(url_for("main"))

    # Delete and commit the transaction
    db.session.delete(recipe_item)
    db.session.commit()

    flash("Recipe deleted successfully.")
    return redirect(url_for("main"))
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
@myapp_obj.route("/logout")
@login_required
def logout():
    logout_user()
    flash("logged out")
    return redirect(url_for("main"))

'route to add a new recipe using GET and POST'

@myapp_obj.route("/recipe/new", methods=['GET', 'POST'])
@login_required
def new_recipe():
    if request.method == "POST":
        'authenticate logged user'
        if not current_user.is_authenticated:
            flash("Please log in")
            return redirect(url_for("login"))

        title = request.form["title"]
        description = request.form["description"]
        ingredients = request.form["ingredients"]
        instructions = request.form["instructions"]

        new_recipe=recipe(title=title,
                          description=description,
                          ingredients=ingredients,
                          instructions=instructions,
                          user_id=current_user.id)
        db.session.add(new_recipe)
        db.session.commit()
        return redirect(url_for("main"))
    return render_template("new_recipe.html")