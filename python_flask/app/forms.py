from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField
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
    remember = BooleanField(label="Remember me")
    submit = SubmitField(label="Log in")


class EditForm(FlaskForm):
    title = StringField(label="Title", validators=[DataRequired(), Length(max=120)])
    markdown = TextAreaField(label="Markdown", validators=[DataRequired()])
    submit = SubmitField(label="Save")
