from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'

@app.route('/count/', methods=['GET', 'POST'])
def count():
    if request.method == 'POST':
        text = request.form.get('text') 
        return f'{len(text)}'
    return render_template('count.html')
    

if __name__ == '__main__':
    app.run(debug=True)
