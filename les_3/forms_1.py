from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()]) # в списке может множество проверок
    password = PasswordField('Password', validators=[DataRequired()])