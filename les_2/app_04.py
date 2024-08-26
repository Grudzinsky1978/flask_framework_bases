# Обработка GET запросов

# Обработка get-запросов является поведением по умолчанию для представлений.

# from flask import request
# ...
#     data = request.args.get('data')
#     ...

# http://127.0.0.1:5000/get/?name=alex&age=13&level=80


from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'

@app.route('/get/')
def get():
    if level := request.args.get('level'): # обращение к свойству args объекта request. args - неизменяемый словарь. У словаря есть метод get
        text = f'Похоже ты опытный игрок, раз имеешь уровень {level}<br>'
    else:
        text = 'Привет, новичок.<br>'
    return f'{text} {request.args}'


if __name__ == '__main__':
    app.run(debug=True)