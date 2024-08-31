# создание форм

# WTForms

    # Определение классов форм
    # Описание полей форм
    # Валидация данных формы

# Описание полей форм

    # ● StringField — строковое поле для ввода текста;
    # ● IntegerField — числовое поле для ввода целочисленных значений;
    # ● FloatField — числовое поле для ввода дробных значений;
    # ● BooleanField — чекбокс;
    # ● SelectField — выпадающий список;
    # ● DateField — поле для ввода даты;
    # ● FileField — поле для загрузки файла.


from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from forms_3 import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'98a1defc494bca05be8beedd6dbd912f2d29aed8dcf7fc8172d279f21d790e47'
csrf = CSRFProtect(app)
"""
Генерация надёжного ключа
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Hi!'


@app.route('/data/')
def data():
    return 'Your data!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        pass
    return render_template('login.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)