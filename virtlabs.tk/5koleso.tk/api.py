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
            Taxi_order.get(id=request.args.get('id')).delete()
    return redirect('/')

@app.route('/application')
def application():
    f = os.path.join(app.root_path, 'static', 'apk', 'forsaje.apk')
    return send_file(f, as_attachment=True, attachment_filename='taxi_forsaje.apk')

# End passenger





# Worker

@app.route('/work/')
def auth_check():
    id = 0
    if request.cookies.get('id'):
        return redirect('/work/index')
    return redirect('/work/auth')

@app.route('/work/auth')
def auth():
    return render_template('work/auth.html')

@app.route('/work/check_worker', methods=['POST'])
def check_worker():
    with db_session:
        user = Auth.get(login=request.form['login'])
        if user:
            if user.password == request.form['password']:
                resp = make_response(redirect('/work/index'))
                resp.set_cookie('id', user.id)
                return resp
    return redirect('/work/auth')

@app.route('/work/index')
def work_index():
    context = {
        "worker_id": request.cookies.get('id')
    }
    return render_template('work/index_w.html', **context)

@app.route('/work/queue')
def queue():
    return render_template('work/queue.html', part=request.args.get('part'))

@app.route('/work/part')
def work_part():
    const = ['', 'Заречный', 'Пенза'] # Constant for directions
    part = int(request.args.get('part'))
    context = dict()
    with db_session:
        worker = Worker.get(id=request.args.get('id'))
        context = {
            'queue': len(Online.select()),
            'position': 1,
            'direction': const[part],
            'orders': Taxi_order.select()
        }
    return render_template('work/orders.html', **context)

@app.route('/work/order')
def order():
    context = {
        'id': request.args.get('id'),
        'phone': request.args.get('phone'),
        'address_from': request.args.get('address_from'),
        'address_to': request.args.get('address_to'),
        'comment': request.args.get('comment'),
        'time_list': [3, 5, 10, 15]
    }
    return render_template('work/order.html', **context)

@app.route('/work/wait_confirm')
def wait_confirm():
    # delete order!!
    context = {
        'id': request.args.get('id'),
        'phone': request.args.get('phone'),
        'address_from': request.args.get('address_from'),
        'address_to': request.args.get('address_to'),
        'comment': request.args.get('comment'),
        'time': request.form['time']
    }
    return render_template('work/wait_confirm.html', **context)

@app.route('/work/lets_go')
def lets_go():
    context = {
        'id': request.args.get('id'),
        'phone': request.args.get('phone'),
        'address_from': request.args.get('address_from'),
        'address_to': request.args.get('address_to'),
        'comment': request.args.get('comment'),
        'time': request.form['time']
    }
    return render_template('/work/lets_go', **context)

@app.route('/work/cancel')
def work_cancel():
    # delete order!!
    return redirect('/work/index')

@app.route('/work/application')
def application_work():
    f = os.path.join(app.root_path, 'static', 'apk', 'work', 'forsaje_work.apk')
    return send_file(f, as_attachment=True, attachment_filename='forsaje_work.apk')
