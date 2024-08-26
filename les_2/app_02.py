# Генерация URL адресов

# При формировании адреса использовать функцию url_for() из модуля Flask:
    # url_for('test_url', num=42, data='new_data', pi=3.14515)

# А в шаблонах используем url_for для указания пути к статике:
    # <img src="{{ url_for('static', filename='image/photo.jpg') }}">

from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'

@app.route('/test_url_for/<int:num>/')
def test_url(num):
    text = f'В num лежит {num}<br>'
    text += f'Функция {url_for("test_url", num=42) = }<br>' # test_url - имя функции, можно изменить пути в route, а имя функции можно не менять
    text += f'Функция {url_for("test_url", num=42, data="new_data") = }<br>' # основная часть, потом ?, потом пары ключ=значение, разделенные &
    text += f'Функция {url_for("test_url", num=42, data="new_data", pi=3.14515) = }<br>'
    return text

if __name__ == '__main__':
    app.run(debug=True)

# В num лежит 7
# Функция url_for("test_url", num=42) = '/test_url_for/42/'
# Функция url_for("test_url", num=42, data="new_data") = '/test_url_for/42/?data=new_data'
# Функция url_for("test_url", num=42, data="new_data", pi=3.14515) = '/test_url_for/42/?data=new_data&pi=3.14515'