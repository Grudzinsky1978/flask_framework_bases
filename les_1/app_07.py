# Шаблонизатор Jinja
# Благодаря Jinja статические html-страницы превращаются в шаблоны для формирования динамических сайтов.
# Функция render_template после имени шаблона может принимать неограниченное число именованных аргументов и пробрасывать их в шаблон.

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'

@app.route('/index/')
def html_index():

    context = {
        'title': 'Личный блог',
        'name': 'Харитон',
    }

    return render_template('index2.html', **context) # распаковка словаря в Jinja. Заменяются имена переменных на значения



if __name__ == '__main__':
    app.run(debug=True)