from flask import Flask, flash, redirect, render_template, url_for
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.fields.simple import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__, template_folder="fe/templates", static_folder="static")
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"


class User(UserMixin, db.Model):  # Модель пользователя
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    mail = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


# Форма регистрации
class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    mail = EmailField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("base.html")


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


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     # Логика входа будет здесь
#     return render_template("login.html")


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True, port=8000)
