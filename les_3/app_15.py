from flask import Flask
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config['SECRET_KEY'] = b'10717e2cd842c394d1992302ce0ec8b630f3f1e905160e947394632e61f2dc1b'
csrf = CSRFProtect(app)
"""
Генерация надёжного ключа
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Hi!'


@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    ...
    return 'No CSRF protection!'



if __name__ == '__main__':
    app.run(debug=True)