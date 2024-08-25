# Наследование шаблонов

# Вывод сложных структур

# {% for user in users %}
#     <h2>{{ user.name }}</h2>
#     <p>{{ user.mail }}</p>
#     <p>{{ user.phone }}</p>
# {% endfor %}


from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'

@app.route('/main/')
def main():
    context = {'title': 'Главная'}
    return render_template('main.html', **context)

@app.route('/data/')
def data():
    context = {'title': 'База статей'}
    return render_template('data.html', **context)


if __name__ == '__main__':
    app.run(debug=True)