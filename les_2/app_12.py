# Flash сообщения

# Flash сообщения во Flask являются способом передачи информации между запросами

    # Функция flash() принимает сообщение и категорию, к которой это сообщение относится, и сохраняет его во временном хранилище
    # app.secret_key обеспечивает работу flash в рамках сессии
    # Функция get_flashed_messages внутри шаблона возвращает все сообщения, переданные через flash и пока не отображённые


from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'
"""
Генерация надёжного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""

@app.route('/')
def index():
    return 'Hi!'


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
    # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')







if __name__ == '__main__':
    app.run(debug=True)