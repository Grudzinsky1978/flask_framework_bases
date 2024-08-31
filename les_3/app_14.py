# Flask WTForm

# pip install Flask-WTF

# Доступ к формам
# from flask_wtf import FlaskForm


# Настройка защиты от CSRF-атак
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'mysecretkey'
# csrf = CSRFProtect(app)


from flask import Flask
from flask_wtf import FlaskForm


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


if __name__ == '__main__':
    app.run(debug=True)