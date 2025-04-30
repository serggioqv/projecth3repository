## Food Recipes

This is a web application that displays a list of recipes created by users.

### Installation

```bash
git clone https://github.com/serggioqv/projecth3repository.git
cd projecth3repository/app131-db
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py

```
Using web browser go to http://127.0.0.1:5000/

### Directory

/ 
for the list of recipes, available to anyone

/recipe/new
In this page you will have a form that will allow you to add a new recipe.

End point displayed only to registered and loged users, use:
User: daniel
Password: 123456

/recipe/<integer>
This page will return one recipe with its details, works only with valid recipe ID 

/recipe/<integer>/delete
This page will delete the specific recipe