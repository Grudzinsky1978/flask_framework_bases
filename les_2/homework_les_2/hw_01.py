from flask import Flask, session, make_response, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b'a0e877221c0a26e299a9ad68e158bde2e4df867fb036043e9c060c4e41b12894'
"""
Генерация надёжного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""

@app.route('/')
def index():
    if 'username' in session:
        return render_template('main.html')
        # return f'Здравствуйте, {session["username"]}!'
    else:
        return redirect(url_for('form'))
    
@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        session['email'] = request.form.get('email') or 'No Email'
        return redirect(url_for('index'))
    return render_template('form.html')

@app.route('/logout/')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    return redirect(url_for('index'))











if __name__ == '__main__':
    app.run(debug=True)