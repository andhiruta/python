from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Andre'}
    posts = [
        {'author': {'username': 'Maria'}, 'body': 'Olá da Maria'},
        {'author': {'username': 'Andre'}, 'body': 'Olá!'}
    ]
    return render_template("index.html", user=user, posts=posts)