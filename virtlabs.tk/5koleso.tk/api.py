import time
import os

from flask import (
                    Flask,
                    render_template,
                    redirect,
                    send_file,
                    request,
                    make_response,
                    session
)
from pony.orm import db_session, select, delete


from initdb import Worker, Auth, Online, Taxi_order


app = Flask(__name__)
app.secret_key = '\x8a<\x1fQ\xf1A#:\xb5A\x18\x8b\xcb\x84\xb9\xe8k\xaf1\xb5\xdc\x04x]'
app.debug = False



import logging
from logging.handlers import SMTPHandler

mail_handler = SMTPHandler(
    mailhost='127.0.0.1:10002',
    fromaddr='nerrevar@server.com',
    toaddrs=['nerrevar12@yandex.ru'],
    subject='Application Error'
)
mail_handler.setLevel(logging.ERROR)
mail_handler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
))

if not app.debug:
    app.logger.addHandler(mail_handler)






@app.route('/robots.txt')
def robots():
    f = os.path.join(app.root_path, 'robots.txt')
    return send_file(f, as_attachment=False, attachment_filename='robots.txt')

from passenger import *

from worker import *

