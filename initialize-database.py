import pymongo
import datetime
import os
from dotenv import load_dotenv

## necessary for python-dotenv ##
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

#mongo = os.getenv('MONGO')
mongo = "mongodb+srv://recipe_user:M2MbzFzEsw2bCsXQ@cluster0.7vqnm.mongodb.net/recipe_db?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo)

db = client['recipe_db']

users = db['users']
roles = db['roles']
recipes = db['recipes']
categories = db['categories']


def add_role(role_name):
    role_data = {
        'role_name': role_name
    }
    return roles.insert_one(role_data)


def add_category(category_name):
    category_data = {
        'category_name': category_name
    }
    return categories.insert_one(category_data)


def add_user(first_name, last_name, email, password, role):
    user_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'role': role,
        'date_added': datetime.datetime.now(),
        'date_modified': datetime.datetime.now()
    }
    return users.insert_one(user_data)


def add_recipe(recipe_name, category, ingredients, preparation, notes, first_name, last_name):
    recipe_data = {
        'recipe_name': recipe_name,
        'category': category,
        'ingredients': ingredients,
        'preparation': preparation,
        'notes': notes,
        'first_name': first_name,
        'last_name': last_name,
        'date_added': datetime.datetime.now(),
        'date_modified': datetime.datetime.now()
    }
    return recipes.insert_one(recipe_data)


def initial_database():
    # add roles
    admin = add_role('admin')
    contributor = add_role('contributor')
    user = add_role('user')

    # add users
    mike = add_user('Nick', 'Acri', 'nick@nick.com', 'abc123', 'admin')

    # add categories
    main = add_category('Main dishes')
    drink = add_category('Appetizer')
    desserts = add_category('Desserts')

   
    # add recipe
    chicken_parmesean = add_recipe('Ravioli', 'Appetizer',
                                   'Pasta', 'at 400', 'cook it real good', 'Nick', 'Acri')


def main():
    initial_database()
   

main()
