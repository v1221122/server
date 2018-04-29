import time
import os


from flask import (
                Flask,
                render_template,
                redirect,
                send_file
)


app = Flask(__name__)

application = app

menu = [
        {
            'img': '/static/img/domovenok.png',
            'href': '/',
            'name': 'Главная'
        },
        {
            'img': '/static/img/knitting.ico',
            'href': '/knitting',
            'name': 'Вязание'
        }
        ]
stylesheet = "style.css"

@app.route('/')
def main():
    items = [
            {
                'target': '#',
                'src': '/static/img/amigurumi1.jpg',
                'title': 'Амигуруми',
                'text': ['амигуруми']
            },
            {
                'target': '#',
                'src': '/static/img/amigurumi.jpg',
                'title': 'Амигуруми',
                'text': ['амигуруми']
            },
            {
                'target': '#',
                'src': '/static/img/amigurumi.jpg',
                'title': 'Амигуруми',
                'text': ['амигуруми']
            }
    ]
    return render_template('index.html', items=items, stylesheet=stylesheet, menu=menu)


@app.route('/knitting')
def knitting():
    items = [
        {
            'target': '#',
            'src': '/static/img/amigurumi.jpg',
            'title': 'Амигуруми',
            'text': ['амигуруми']
        }
    ]
    return render_template('index.html', items=items, stylesheet=stylesheet, menu=menu)


@app.route('/favicon.ico')
def favicon():
    f = os.path.join(app.root_path, 'static', 'img', 'favicon.ico')
    return send_file(f, as_attachment=False, attachment_filename='favicon.ico')
