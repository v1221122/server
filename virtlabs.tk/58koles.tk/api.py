import time
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def main():
    items = [
            {
                'target': 'http://forsaje.tk/application',
                'src': '/static/img/forsaje.jpg',
                'title': 'Приложение ТАКСИ Forsaje',
                'text': ['Приложение такси Forsaje можно скачать <a href="http://forsaje.tk/application">здесь</a>.']
            },
            {
                'target': '#',
                'src': '/static/img/renault.jpg',
                'title': 'Пассажирские перевозки',
                'text': ['свадьбы', 'юбилеи', 'межгород'],
                'list': True
            }
    ]
    stylesheet = "style.css"
    return render_template('index.html', items=items, stylesheet=stylesheet)
