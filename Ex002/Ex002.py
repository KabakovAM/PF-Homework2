from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from pathlib import PurePath, Path

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'

@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'Homework2/Ex002/uploads', file_name))
        return f'Файл {file_name} загружен на сервер'
    return render_template('upload.html')
    

if __name__ == '__main__':
    app.run(debug=True)
