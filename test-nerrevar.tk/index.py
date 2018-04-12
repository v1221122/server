from flask import *

from pony.orm import *

app = Application = Flask(__name__)

@app.route('/')
def index():
    context = {
                'data':[
                        {
                            'art': u'25ол8',
                            'desc': u'мышь'
                        }
                ]
    }
    return render_template('index.html', **context)
