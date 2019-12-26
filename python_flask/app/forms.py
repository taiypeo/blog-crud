from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField(
        label="Username", validators=[DataRequired(), Length(max=30)]
    )
    password = PasswordField(
        label="Password", validators=[DataRequired(), Length(max=150)]
    )
    confirm_password = PasswordField(
        label="Confirm password",
        validators=[DataRequired(), Length(max=150), EqualTo("password")],
    )
    submit = SubmitField(label="Register")


class LoginForm(FlaskForm):
    username = StringField(
        label="Username", validators=[DataRequired(), Length(max=30)]
    )
    password = PasswordField(
        label="Password", validators=[DataRequired(), Length(max=150)]
    )
    submit = SubmitField(label="Log in")
