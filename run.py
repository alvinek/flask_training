from flask import Flask
from flask import render_template
from flask import request
from flask import abort, send_from_directory
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')


@app.route('/contact')
def contact():
    return "<h1 style='color:pink'>Contact</h1>"


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/user/<username>', methods=['GET', 'POST'])
def show_user_profile(username):
    if request.method == 'POST':
        return 'HTTP post user %s password %s' % (username, request.form['password'])
    else:
        return 'HTTP get for user %s' % username


@app.route('/error_denied')
def error_denied():
    abort(401)


if __name__ == '__main__':
    app.run(debug=True)
