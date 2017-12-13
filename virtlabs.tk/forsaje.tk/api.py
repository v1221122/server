import time
import os
from flask import Flask, render_template, redirect, send_file

app = Flask(__name__)

@app.route('/')
def main():
    context = {
                'cars': 1,
                'body': 'hello world!',
    }
    return render_template('index_p.html', **context)

   
@app.route('/get_form')
def get_form():
    return render_template('get_form.html')
    
    
@app.route('/wait')
def wait():
    current_car = {
                    'name': 'wv',
                    'color': 'синий',
                    'number': 466,
    }
    time = 5
    if current_car:
        pass
    return render_template('wait.html', car = current_car, time = time)
    
    
@app.route('/wait_page')
def wait_page():
    confirm = False
    time = 5
    current_car = {
                    'name': 'wv',
                    'color': 'синий',
                    'number': 466,
    }
    return render_template('wait_page.html', car = current_car, time = time * 60, confirm = confirm)
    
    
@app.route('/cancel')
def cancel():
    #delete!!!
    return redirect('/')

@app.route('/application')
def application():
    f = os.path.join(app.root_path, 'static', 'apk', 'forsaje.apk')
    return send_file(f, as_attachment=True, attachment_filename='taxi_forsaje.apk')

