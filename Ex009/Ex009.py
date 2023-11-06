from flask import Flask, render_template, request, redirect, make_response, url_for
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()

@app.route('/')
def index():
    return 'Hello'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    response = make_response(render_template('login.html'))
    response.set_cookie('name', max_age=0)
    response.set_cookie('email', max_age=0)
    if request.method == 'POST':
        name = request.form.get('name') 
        email = request.form.get('email')
        response = make_response(redirect(url_for('logout', name=name)))
        response.set_cookie('name', name)
        response.set_cookie('email', email)
    return response

@app.route('/logout/<name>/', methods=['GET', 'POST'])
def logout(name):
    context= {'name': name}
    if request.method == 'POST':
        return redirect(url_for('login'))      
    return render_template('logout.html', **context)
    

if __name__ == '__main__':
    app.run(debug=True)
