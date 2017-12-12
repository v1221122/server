import time
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def main():
    items = [{
                'src': '/static/img/renault.jpg',
                'title': '<div style="margin-left:30%; margin-right:30%">Пассажирские<br>перевозки</div>',
                'text': '<p>paragraph1</p><p>paragraph2</p>'
            },
            {
                'src': '/static/img/forsaje.jpg',
                'title': 'Forsaje',
                'text': 'this is text about forsaje'
            }
    ]
    stylesheet = "style.css"
    return render_template('index.html', items=items, stylesheet=stylesheet)
