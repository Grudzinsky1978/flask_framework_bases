from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegForm(FlaskForm):
    u_name = StringField('Имя', validators=[DataRequired(), Length(min=2, max=30)])
    u_surname = StringField('Фамилия', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    passw = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    confirm_passw = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('passw')])