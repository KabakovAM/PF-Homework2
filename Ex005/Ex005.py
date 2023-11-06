from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'

@app.route('/calc/', methods=['GET', 'POST'])
def calc():
    result = 0
    if request.method == 'POST':
        a = int(request.form.get('a'))
        b = int(request.form.get('b'))
        op = request.form.get('operation')
        if op == 'add':
            result = a + b
        if op == 'sub':
            result = a - b  
        if op == 'mult':
            result = a * b  
        if op == 'div':
            result = a / b  
        return f'{result}'
    return render_template('calc.html')
    

if __name__ == '__main__':
    app.run(debug=True)
