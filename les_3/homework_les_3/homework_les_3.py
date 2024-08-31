from flask import Flask, render_template, request, redirect
from model import db, User
from flask_wtf.csrf import CSRFProtect

from form import RegForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'90eab01de91544f939d06a892e158ed2f1a93a60b693d9e538746e71ee66da94'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
csrf = CSRFProtect(app)
db.init_app(app)
"""
Генерация надёжного ключа
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Hi!'


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/reg/', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if request.method == 'POST' and form.validate():
        u_name = form.u_name.data
        u_surname = form.u_surname.data
        email = form.email.data
        passw = form.passw.data
        user = User(u_name=u_name, u_surname=u_surname, email=email, passw=passw)
        db.session.add(user)
        db.session.commit()
        return f'{u_surname} {u_name}, вы успешно заргистрировались!'
    return render_template('reg.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)