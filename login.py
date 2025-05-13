from flask import request, Blueprint
from utilities import get_html,usersdb

login_bp = Blueprint("login","book")

# Get submitted form data using request.form.get('email') and request.form.get('password').
 
   
# Validate that the fields are not empty.

# Load your users data (e.g., from JSON file or database).

# Check if a user with the submitted email exists.

# Verify if the submitted password matches the stored password for that user.
def do_login():
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password","").strip()
    user_log = {
        "email": email,
        "password": password
    }
    # checking for empty fields
    for key,value in user_log.items():
        if not value:
            return f"please enter your {key}"
    # get json file from usersdb()
    users = usersdb()
    for user in users:
        if user_log.get("email") == user.get("email"):
            print(f"Comparing passwords: input='{password}' stored='{user.get('password')}'")
            if user_log.get("password") == user.get("password"):
                return get_html("home")
            else:
                return "Password is not correct"
    return "User name is not correct"
 

def show_login():
    return get_html("login")

@login_bp.route('/login', methods=['GET', 'POST'])
def logging():
    if request.method == 'POST':
        return do_login()
    else:
        return show_login()