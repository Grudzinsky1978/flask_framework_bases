# Использование форм в приложении

# * Отображение форм на страницах приложения
# * Обработка данных из формы



from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from forms_3 import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'964093fe6e6b3702e99d39ade77fccc77571f071c95906914e571f97c292fb6a'
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


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        email = form.email.data # обращаемся к данным, которые лежат в свойстве
        password = form.password.data
        print(email, password)
        ...
    return render_template('register.html', form=form)




if __name__ == '__main__':
    app.run(debug=True)