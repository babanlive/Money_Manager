from app.edit.edit import edit
from flask import Flask, abort, render_template, session, redirect, url_for, request
from app.crud import create_user
import os


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.secret_key = os.urandom(32)
    app.register_blueprint(edit, url_prefix='/edit')

    @app.route("/")
    def index():
        return render_template("home.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if "userLogged" in session:
            return redirect(url_for("profile", username=session["userLogged"]))
        elif (
            request.method == "POST"
            and request.form["login"] == "asd"
            and request.form["password"] == "zxc"
        ):
            session["userLogged"] = request.form["login"]
            return redirect(url_for("profile", username=session["userLogged"]))
        return render_template(
            "login.html",
        )

    @app.route("/profile/<username>")
    def profile(username):
        print(session)
        if "userLogged" not in session or session["userLogged"] != username:
            abort(401)

        return f"Профиль {username}"

    @app.route("/signup", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            username = request.form["login"]
            password = request.form["password"]
            create_user(login=username, password=password)
        return render_template("registration.html")

    

    
 
    return app
