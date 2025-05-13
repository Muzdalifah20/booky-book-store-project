from flask import request, Blueprint
import json
from utilities import get_html, usersdb
register_bp = Blueprint("register","book")

def do_register():
   
     first_name = request.form.get("first_name").strip().lower()
     last_name = request.form.get("last_name").strip().lower()
     email = request.form.get("email").strip().lower()
     password = request.form.get("password")
     new_user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password
     }
     # checking for empty fields
     for key,value in new_user.items():
          if not value:
               return f"please enter your {key}"
     # get json file fron usersdb()
     users = usersdb()
    
     # handling duplicate emails
     for user in users:
          if new_user["email"] == user["email"]:
               return f"This email already exists"
     # append the new_user to users only if the email not found
     users.append(new_user)
     # save the new_user to json file
     with open("usersdb.json","w") as file:
          json.dump(users, file, indent=4)
     return "Succesfuly registerd!"
 
 
def show_register():
     return get_html("register") 


@register_bp.route('/register', methods=['GET', 'POST'])
def registeration():
    if request.method == 'POST':
        return do_register()
    else:
        return show_register()
 
