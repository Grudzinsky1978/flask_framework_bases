# Экранирование пользовательских данных
# Для повышения безопасности нужно экранировать ввод пользователя - используйте функцию escape из модуля markupsafe.

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Введите путь к файлу в адресной строке'

@app.route('/<path:file>/')
def get_file(file):
    print(file)
    # return f'Ваш файл находится в: {file}!' # если в адресной строке ввести <script>alert("I%20am%20haсker")</script>, то можно запустить скрипт, что небезопасно
    return f'Ваш файл находится в: {escape(file)}!' # скрипт не запускается


if __name__ == '__main__':
    app.run(debug=True)