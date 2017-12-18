import time
import os

from flask import Flask, render_template, redirect, send_file, request
from pony.orm import db_session, select, delete


from initdb import Worker, Auth, Online, Taxi_order

app = Flask(__name__)

# Passenger

@app.route('/')
def main():
    with db_session:
        query = Online.select()
        context = {
                    'cars': len(query),
        }
        return render_template('index_p.html', **context)

   
@app.route('/get_form')
def get_form():
    return render_template('get_form.html')
  

@app.route('/commit')  
def commit_to_db():
    d = request.args.to_dict()
    order = {
        'phone': d['phone'],
        'address_from': 'ул. {} д. {} к. {} п. {}'.format(d['street'], d['dom'], d['korp'], d['pod']),
        'address_to': d['dest'],
        'comment': d['comment']
    }
    with db_session:
        try:
            added_order = Taxi_order(**order)
            return redirect('/wait?phone=' + d['phone'])
        except:
            return redirect('/')
    
@app.route('/wait')
def wait():
    current_car = dict()
    id = 0
    with db_session:
        order = Taxi_order.get(phone=request.args.get('phone'))
        if order:
            if order.worker_id:
                worker = Worker.get(id=order.worker_id)
                current_car = {
                    'car': worker.car,
                    'color': worker.color,
                    'number': worker.number,
                }
                id = order.id
    time = 5
    context = {
        'car': current_car,
        'time': time,
        'refresh': True,
        'id': id
    }
    return render_template('wait.html', **context)
    
    
@app.route('/wait_page')
def wait_page():
    confirm = False
    time = request.args.get('time') - 1
    current_car = dict()
    with db_session:
        order = Taxi_order.get(id=request.args.get('id'))
        if order:
            if order.worker_id:
                worker = Worker.get(id=order.worker_id)
                current_car = {
                    'car': worker.car,
                    'color': worker.color,
                    'number': worker.number,
                }
    context = {
        'car': current_car,
        'time': time,
        'confirm': confirm,
        'refresh': True,
        'id': order.id
    }
    return render_template('wait_page.html', **context)
    
    
@app.route('/cancel')
def cancel():
    with db_session:
        if request.args.get('id'):
            Taxi_order.get(request.args.get('id')).delete()
    return redirect('/')

@app.route('/application')
def application():
    f = os.path.join(app.root_path, 'static', 'apk', 'forsaje.apk')
    return send_file(f, as_attachment=True, attachment_filename='taxi_forsaje.apk')

# End passenger

# Worker

@app.route('/work/')
def work():
    return render_template('work/auth.html')

@app.route('/work/index')
def work_index():
    context = {
        "worker_id": request.args.get('worker_id')
    }
    return render_template('work/index_w.html', **context)
    
@app.route('/work/check_worker')
def check_worker():
    #check login
    id = 1
    return redirect('/work/index?worker_id=' + id)
    
@app.route('/work/zarechny')
def work_zarechny():
    context = {
        'queue': 1,
        'position': 1
    }
    return render_template('work/zarechny.html', **context)
    
@app.route('/work/order_zarechny')
def order_zarechny():
    with db_session:
        orders = Taxi_order.select()
        if orders:
            o = list()
            for order in orders:
                o.append({
                            'phone': order.phone,
                            'address_from': order.address_from,
                            'address_to': order.address_to,
                            'comment': order.comment
                        })
                context = {
                    'orders': o
                }
        else:
            context = dict()
    return render_template('work/order_zarechny.html', **context)
    

@app.route('/work/application')
def application_work():
    f = os.path.join(app.root_path, 'static', 'apk', 'work', 'forsaje_work.apk')
    return send_file(f, as_attachment=True, attachment_filename='forsaje_work.apk')
