from flask import render_template,request, redirect
from users_app import app 
from users_app.models.User import User

@app.route( "/users", methods=['GET'] )
def getAllUsers():
    users = User.get_all_users()
    return render_template( "read.html", users=users )

@app.route("/users/add")
def render_create():
    return render_template("create.html")

@app.route("/users/add", methods=['POST', 'GET'])
def addUser():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    newUser = User(first_name,last_name,email)
    result = User.add_user(newUser)

    return redirect ("/users")