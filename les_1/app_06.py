from flask import Flask
from flask import render_template # отрисовка шаблона, используется для шаблонизатора Jinja

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'

@app.route('/index/')
def html_index():
    return render_template('index1.html') # ищется только в подкаталоге templates, если нет каталога - вызовет ошибку



if __name__ == '__main__':
    app.run(debug=True)