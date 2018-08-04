import os
from flask import Flask, render_template, session, redirect, url_for, escape, request, make_response, jsonify
from flask_compress import Compress

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# Compress data if needed
Compress(app)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/')
def index():
    if 'username' in session:
        resp = 'Logged in as %s' % escape(session['username'])
    else:
        resp = 'You are not logged in'
    return resp + " Hello i'm TelegrammBot!"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/get_webhook')
def get_webhook():
    searchword = request.args.get('key', '')
    return searchword


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['test_data'] = 'my_test_is a good idea'
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/get_corrent_data')
def get_corrent_data():
    if request.method == 'GET':
        return jsonify(list(range(3000)))
    else:
        redirect(url_for('/'))


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
