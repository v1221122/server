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

from api import app

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
                resp.set_cookie('id', str(user.id))
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
            'orders': Taxi_order.select(),
            'refresh': True
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
    context = {
        'id': request.args.get('id'),
        'phone': request.args.get('phone'),
        'address_from': request.args.get('address_from'),
        'address_to': request.args.get('address_to'),
        'comment': request.args.get('comment'),
        'time': request.args.get('time')
    }
    with db_session:
        select(p for p in Taxi_order if p.phone == context['phone']).delete()
    return render_template('work/wait_confirm.html', **context)

@app.route('/work/confirm')
def confirm():
    context = {
        'id': request.args.get('id'),
        'phone': request.args.get('phone'),
        'address_from': request.args.get('address_from'),
        'address_to': request.args.get('address_to'),
        'comment': request.args.get('comment'),
        'time': request.args.get('time')
    }
    return render_template('work/confirm.html', **context)

@app.route('/work/lets_go')
def lets_go():
    context = {
        'id': request.args.get('id'),
        'phone': request.args.get('phone'),
        'address_from': request.args.get('address_from'),
        'address_to': request.args.get('address_to'),
        'comment': request.args.get('comment'),
        'time': request.args.get('time')
    }
    return render_template('/work/lets_go.html', **context)

@app.route('/work/cancel')
def work_cancel():
    return redirect('/work/index')

@app.route('/work/end_order')
def end_order():
    try:
        select(p for p in Taxi_order if p.id == request.args.get('id')).delete()
    except:
        return redirect('/work/index')


@app.route('/work/application')
def application_work():
    f = os.path.join(app.root_path, 'static', 'apk', 'work', 'forsaje_work.apk')
    return send_file(f, as_attachment=True, attachment_filename='forsaje_work.apk')

@app.route('/work/info')
def info():
    return render_template('/work/info.html')