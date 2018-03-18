#-*- coding:utf-8 -*-

from flask import (
            render_template,
            Flask
            )

app = Flask(__name__)
app.secret_key = '\x8a<\x1fQ\xf1A#:\xb5A\x18\x8b\xcb\x84\xb9\xe8k\xaf1\xb5\xdc\x04x]'

application = app

@app.route('/')
def index():
    return render_template('authorization.html')


@app.route('/authorized')
def authorized():
    return render_template('authorized.html')