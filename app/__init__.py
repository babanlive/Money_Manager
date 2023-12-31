from app.user.views import blueprint as user_blueprint
from app.edit.edit import edit
from flask import Flask, abort, render_template
from flask import session
import os


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.secret_key = os.urandom(32)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(edit, url_prefix='/edit')

    @app.route("/")
    def index():
        return render_template("home.html")

    @app.route("/profile/<username>")
    def profile(username):
        print(session)
        if "userLogged" not in session or session["userLogged"] != username:
            abort(401)
        return f"Профиль {username}"

    return app
