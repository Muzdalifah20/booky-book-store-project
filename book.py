from flask import Flask, request
import json
from register import register_bp
from login import login_bp
from utilities import get_html, usersdb
app = Flask("book")

app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
 

@app.route("/")
@app.route("/home")
def homepage():
     return get_html("home")

# @app.route("/register")
# def show_register():
#           return get_html("register")

 

 


if __name__ == "__main__" :
    app.run(debug=True)
