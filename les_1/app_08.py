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

@app.route('/if/')
def show_if():

    context = {
        'title': 'Ветвление',
        'user': 'Крутой хакер!',
        'number': 1,
    }

    return render_template('show_if.html', **context) # распаковка словаря в Jinja



if __name__ == '__main__':
    app.run(debug=True)