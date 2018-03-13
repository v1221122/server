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

@app.route('/robots.txt')
def robots():
    f = os.path.join(app.root_path, 'robots.txt')
    return send_file(f, as_attachment=False, attachment_filename='robots.txt')

from passenger import *

from worker import *
