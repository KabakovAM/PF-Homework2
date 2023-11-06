from flask import Flask, render_template, request, redirect, url_for, flash
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()

@app.route('/')
def index():
    return 'Hello'

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        if not request.form['name']:
            return redirect(url_for('form'))
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash.html')
    

if __name__ == '__main__':
    app.run(debug=True)
