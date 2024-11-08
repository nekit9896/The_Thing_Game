from flask import flash, redirect, url_for, render_template
from flask_login import LoginManager

from be.app import app
from be.form_datas import RegistrationForm
from be.table_models import User, db

login_manager = LoginManager(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            mail=form.mail.data,
            password=form.password.data,  # В реальном приложении необходимо хешировать пароль
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully!", "success")
        return redirect(url_for("login"))
    return render_template("registration.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    # Логика входа будет здесь
    return render_template("login.html")
