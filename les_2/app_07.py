# Загрузка файлов через POST запрос

# обязательный минимум:

    # enctype=myltipart/form-data в HTML форме
    # file = request.files.get('file') при получении файла в POST view
    # file.save для сохранения файла

    # from werkzeug.utils import secure_filename - дополнительное преобразование имени для безопасности

from pathlib import PurePath, Path
from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)