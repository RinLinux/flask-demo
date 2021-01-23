from flask import Flask,render_template,url_for
from form import RegistrationForm, LoginForm

import secrets

key = secrets.token_hex(16)

app = Flask(__name__)

app.config['SECRET_KEY'] = key

posts = [
    {
        'author':'Mike',
        'title':'Flask Post 1',
        'content':'First Flask blog post.',
        'date_posted':'22, Jan, 2021'
    },
    {
        'author':'Jim',
        'title':'Flask Post 2',
        'content':'Second Flask blog post.',
        'date_posted':'23, Jan, 2021'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title = 'About')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html',title="Register",form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title="Login",form=form)


if __name__ == '__main__':
    app.run(debug=True)
