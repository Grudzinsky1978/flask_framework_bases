from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    context = {'title': 'Главная'}
    return render_template('main.html', **context)

@app.route('/clothes/')
def clothes():
    context = {'title': 'Одежда'}
    return render_template('clothes.html', **context)

@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    return render_template('shoes.html', **context)

@app.route('/jackets/')
def jackets():
    context = {'title': 'Куртки'}
    return render_template('jackets.html', **context)


if __name__ == '__main__':
    app.run(debug=True)