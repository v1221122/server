import time
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def main():
    items = [
            {
                'target': 'http://forsaje.tk/application',
                'src': '/static/img/forsaje.jpg',
                'title': 'Приложение Forsaje',
                'text': 'Приложение такси'
            },
            {
                'target': '#',
                'src': '/static/img/renault.jpg',
                'title': 'Пассажирские перевозки',
                'text': 'paragraph1<br>paragraph2'
            }
    ]
    stylesheet = "style.css"
    return render_template('index.html', items=items, stylesheet=stylesheet)
