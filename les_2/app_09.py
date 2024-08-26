# Обработка ошибок

# ---
# Функция abort
# Может использоваться внутри view функций. Получив 404, прерывается работа текущей view и вызывается функция, которая декорирована errorhandler

# if result is None:
#     abort(404)



from flask import Flask
from flask import render_template
from flask import request
from flask import abort

from db import get_blog

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


@app.route('/blog/<int:id>')
def get_blog_by_id(id):
    ...
    # делаем запрос в БД для поиска статьи по id
    result = get_blog(id)
    if result is None:
        abort(404)
    ...
    # возвращаем найденную в БД статью


@app.errorhandler(404) # декоратор обрабатывает 404 ошибку
def page_not_found(e):
    app.logger.warning(e) # логирование в консоль
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404


if __name__ == '__main__':
    app.run(debug=True)