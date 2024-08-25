# Помимо простой передачи {{ variable }} в шаблонах можно использовать ветвления и циклы

# {% if ... %}
# value
# {% elif ... %}
# value
# {% else ... %}
# value
# {% endif %}


# {% for item in list %}
# {{ item }}
# {% endfor %}


from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'

@app.route('/for/')
def show_for():
    context = {'title': 'Цикл',
    'poem': ['Вот не думал, не гадал,',
            'Программистом взял и стал.',
            'Хитрый знает он язык,',
            'Он к другому не привык.',
            ]
    }
    # txt = '<h1>Стихотворение</h1>\n<p>' + '<br>'.join(poem) + '</p>'
    return render_template('show_for.html', **context)

if __name__ == '__main__':
    app.run(debug=True)