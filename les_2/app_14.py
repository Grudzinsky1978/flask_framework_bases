# Работа с cookie файлами во Flask

# cookie файлы - небольшие текстовые файлы, которые хранятся в браузере пользователя и используются для хранения информации о пользователе и его предпочтениях на сайте

# ...
# response = make_response('Cookie установлен')
# response.set_cookie('username', 'admin')
# ...
# name = request.cookies.get('username')

# Функция make_response() создаёт объект ответа. Если возвращать не результат её работы, функция неявно создаёт объект ответа.


from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    # устанавливаем cookie
    response = make_response("Cookie установлен")
    response.set_cookie('username', 'admin')
    return response

@app.route('/getcookie/') # Чтобы посмотреть, как выглядят cookie
def get_cookies():
    # получаем значение cookie
    name = request.cookies.get('username')
    return f"Значение cookie: {name}"



if __name__ == '__main__':
    app.run(debug=True)