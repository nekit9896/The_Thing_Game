from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


# Форма регистрации
class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    mail = EmailField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")