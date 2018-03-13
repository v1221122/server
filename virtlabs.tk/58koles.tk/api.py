import time
import os


from flask import (
                Flask,
                render_template,
                redirect,
                send_file
)


app = Flask(__name__)


@app.route('/')
def main():
    items = [
            {
                'target': 'http://5koleso.tk/application',
                'src': '/static/img/forsaje.jpg',
                'title': 'Приложение ТАКСИ Forsaje',
                'text': ['Приложение такси Forsaje можно скачать <a href="http://5koleso.tk/application">здесь</a>.']
            },
            {
                'target': '#',
                'src': '/static/img/renault.jpg',
                'title': 'Пассажирские перевозки<br>8-927-381-55-95',
                'text': ['свадьбы', 'юбилеи', 'межгород'],
                'list': True
            }
    ]
    stylesheet = "style.css"
    return render_template('index.html', items=items, stylesheet=stylesheet)


@app.route('/favicon.ico')
def robots():
    f = os.path.join(app.root_path, 'static', 'img', 'favicon32x32.ico')
    return send_file(f, as_attachment=False, attachment_filename='favicon.ico')
