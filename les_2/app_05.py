# Обработка POST запросов
# post-запросы используются для отправки данных на сервер. Обычно используют HTML-форму:

# <form action="/submit" method="post">
#     <input type="text", name="name", placeholder="Имя">
#     <input type="submit", value="Отправить">
# </form>



from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'

@app.route('/submit', methods=['GET', 'POST']) # указали, что функция может работать и с get и с post запросами
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)