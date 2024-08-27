# Обработка ошибок

# ---
# Декоратор errorhandler

# @app.errorhandler(404)
# def page_not_found(e):
#     ...
#     return render_template('404.html', **context), 404

# ---
# Функция abort

# if result is None:
#     abort(404)

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

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


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