import time
import os
from math import fabs

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


timer = { 
        'now': time.time(),
        '1': 0
}  # List for worker's timers  


flag = False
time_flag = False

@app.route('/work/')
def auth_check():
    id = 0
    if request.cookies.get('id'):
        return redirect('/work/index')
    return redirect('/work/auth')

@app.route('/work/auth')  # Authentication  
def auth():
    return render_template('work/auth.html')

@app.route('/work/check_worker', methods=['POST'])  # Check authentication  
def check_worker():
    with db_session:
        user = Auth.get(login=request.form['login'])
        if user:
            if user.password == request.form['password']:
                resp = make_response(redirect('/work/index'))
                resp.set_cookie('id', str(user.id))
                return resp
    return redirect('/work/auth')

@app.route('/work/index')  # Main page  
def work_index():
    context = {
        "worker_id": request.cookies.get('id'),
        'back': 'logout'
    }
    return render_template('work/index_w.html', **context)

@app.route('/work/queue')  # Page to enter the queue  
def queue():
    return render_template('work/queue.html', part=request.args.get('part'), back='index')

@app.route('/work/part')  # Page with waiting the orders  
def work_part():
    const = ['', 'Заречный', 'Пенза']  # Constant for directions  
    part = int(request.args.get('part'))
    context = dict()
    with db_session:
        worker = Worker.get(id=request.args.get('id'))
        context = {
            'queue': len(Online.select()),
            'position': 1,
            'direction': const[part],
            'orders': Taxi_order.select(),
            'refresh': True,
            'back': 'index'
        }
        return render_template('work/orders.html', **context)

@app.route('/work/order')  # Selected order details  
def order():
    context = {
        'id': request.args.get('id'),
        'phone': request.args.get('phone'),
        'address_from': request.args.get('address_from'),
        'address_to': request.args.get('address_to'),
        'comment': request.args.get('comment'),
        'time_list': [3, 5, 10, 15],
        'back': 'part'
    }
    return render_template('work/order.html', **context)

@app.route('/work/wait_confirm')  # Page with stopped timer  
def wait_confirm():
    context = {
        'id': request.args.get('id'),
        'phone': request.args.get('phone'),
        'address_from': request.args.get('address_from'),
        'address_to': request.args.get('address_to'),
        'comment': request.args.get('comment'),
        'time': request.args.get('time'),
        'refresh': True
    }
    timer[request.cookies.get('id')] = time.time() + float(context['time'])*60
    p_confirm = False
    with db_session:
        order = select(p for p in Taxi_order if p.phone == context['phone'])
        for o in order:
            o.worker_id = request.cookies.get("id")
            o.time = context['time']
            p_confirm = o.p_confirm
    global flag
    flag = True
    return render_template('work/wait_confirm.html', **context)  # !!!! add timer start

    
@app.route('/work/confirm')  # Page with timer  
def confirm():
    context = {
        'id': request.args.get('id'),
        'phone': request.args.get('phone'),
        'address_from': request.args.get('address_from'),
        'address_to': request.args.get('address_to'),
        'comment': request.args.get('comment'),
        'time':{
                'int': int((timer[request.cookies.get('id')] - time.time()) // 60),
                'float': '{:0>2.0f}'.format(fabs(timer[request.cookies.get('id')] - time.time()) % 60)
        },
        'refresh': True
    }
    global flag
    if flag:
        with db_session:
            order = select(p for p in Taxi_order if p.phone == context['phone'])
            for o in order:
                o.w_confirm = True
        flag = False
        global time_flag
        time_flag = True
    return render_template('work/confirm.html', **context)

@app.route('/work/lets_go')  # Go go go  
def lets_go():
    global time_flag
    if time_flag:
        timer[request.cookies.get('id')] = time.time()
        time_flag = False
    context = {
        'id': request.args.get('id'),
        'phone': request.args.get('phone'),
        'address_from': request.args.get('address_from'),
        'address_to': request.args.get('address_to'),
        'comment': request.args.get('comment'),
        'time':{
                'int': int((time.time() - timer[request.cookies.get('id')]) // 60),
                'float': '{:0>2.0f}'.format((time.time() - timer[request.cookies.get('id')]) % 60)
        },
        'refresh': True
    }
    return render_template('/work/lets_go.html', **context)

@app.route('/work/cancel')  # Cancelling order  
def work_cancel():
    # update worker_id in order!!!!
    return redirect('/work/index')

@app.route('/work/end_order')  # Ending order  
def end_order():
    with db_session:
        select(p for p in Taxi_order if p.id == request.args.get('id')).delete()  # need to store order and then delete and delete worker from queue!!!!
    return redirect('/work/index')
    
@app.route('/work/exit_queue')
def exit_queue():
    pass
    


@app.route('/work/application')  # Apk file  
def application_work():
    f = os.path.join(app.root_path, 'static', 'apk', 'work', 'forsaje_work.apk')
    return send_file(f, as_attachment=True, attachment_filename='forsaje_work.apk')

@app.route('/work/info')  # Info page  
def info():
    return render_template('/work/info.html', back='index')