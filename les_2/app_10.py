# Обработка ошибок

# ---
# Некоторые коды ошибок

    # 400: Неверный запрос
    # 401: Не авторизован
    # 403: Доступ запрещён
    # 404: Страница не найдена
    # 500: Внутренняя ошибка сервера



from flask import Flask
from flask import render_template
from flask import request
from flask import abort

# from db import get_blog # Специально сломали импорт

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


@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404

@app.errorhandler(500)
def page_not_found(e):
    app.logger.error(e)
    context = {
        'title': 'Ошибка сервера',
        'url': request.base_url,
    }
    return render_template('500.html', **context), 500


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=False)