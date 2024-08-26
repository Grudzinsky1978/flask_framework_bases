# Перенаправления

# с одной страницы на другую

# from flask import redirect, url_for
# ...
# @app_route('/redirect/')
# def redirect_to_index():
#     return redirect(url_for('index'))
# ...


from flask import Flask
from flask import redirect
from flask import url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'

@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('index'))

@app.route('/external')
def external_redirect():
    return redirect('https://www.python.org')

@app.route('/hello/<name>')
def hello(name):
    return f'Привет, {name}!'

@app.route('/redirect/<name>')
def redirect_to_hello(name):
    return redirect(url_for('hello', name=name))



if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)