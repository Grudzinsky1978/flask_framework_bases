# Замена route на get и post
# Функция-представление может быть разделена на две, каждая обрабатывает свой вид запроса.

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'

@app.get('/submit')
def submit_get():
    return render_template('form.html')

@app.post('/submit')
def submit_post():
    name = request.form.get('name')
    return f'Hello {name}!'


if __name__ == '__main__':
    app.run(debug=True)