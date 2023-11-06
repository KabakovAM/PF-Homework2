from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'

@app.route('/login/', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        login = request.form.get('login') 
        password = request.form.get('password') 
        if login == '1' and password == '2':
            return f'Привет {login}'
        else:
            return f'Error'
    return render_template('login.html')
    

if __name__ == '__main__':
    app.run(debug=True)
