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


from initdb import Online, Taxi_order, Worker

from api import app

@app.route('/')  # Greeting page
def main():
    with db_session:
        query = Online.select()
        context = {
                    'cars': len(query),
        }
        return render_template('index_p.html', **context)


@app.route('/get_form')  # Page with order info input
def get_form():
    return render_template('get_form.html')


@app.route('/commit')  # Function to write order data to database
def commit_to_db():
    d = request.args.to_dict()
    order = {
        'phone': d['phone'],
        'address_from': 'ул. {} д. {} к. {} п. {}'.format(d['street'], d['dom'], d['korp'], d['pod']),
        'address_to': d['dest'],
        'comment': d['comment']
    }
    with db_session:
        if order['phone']:
            try:
                added_order = Taxi_order(**order)
                resp = make_response(redirect('/wait'))
                resp.set_cookie('user_phone', order['phone'])
                return resp
            except:
                return redirect('/')
        else:
            return redirect('/')

@app.route('/wait')  # Page with car description and time
def wait():
    current_car = dict()
    id = 0
    with db_session:
        order = Taxi_order.get(phone=request.cookies.get('user_phone'))
        if order:
            if order.worker_id:
                worker = Worker.get(id=order.worker_id)
                current_car = {
                    'car': worker.car,
                    'color': worker.color,
                    'number': worker.number
                }
    time = 5 # !!!!
    context = {
        'car': current_car,
        'time': time,
        'refresh': True
    }
    return render_template('wait.html', **context)


@app.route('/wait_page')  # Page with timer
def wait_page():
    confirm = False
    time = request.args.get('time')
    current_car = dict()
    with db_session:
        order = Taxi_order.get(phone=request.cookies.get('user_phone'))
        if order:
            if order.worker_id:
                worker = Worker.get(id=order.worker_id)
                current_car = {
                    'car': worker.car,
                    'color': worker.color,
                    'number': worker.number,
                }
                confirm = order.w_confirm
    context = {
        'car': current_car,
        'time': time, # !!!!
        'confirm': confirm,
        'refresh': True
    }
    return render_template('wait_page.html', **context)


@app.route('/complete')  # Function to end order
def complete():
    with db_session:
        if request.cookies.get('user_phone'):
            phone = request.cookies.get('user_phone')
            select(p for p in Taxi_order if p.phone == phone).p_confirm = True
    return redirect('/')

@app.route('/cancel')  # Function to cancel order
def cancel():
    with db_session:
        if request.cookies.get('user_phone'):
            phone = request.cookies.get('user_phone')
            select(p for p in Taxi_order if p.phone == phone).delete()
    return redirect('/')






@app.route('/application')  # Apk file
def application():
    f = os.path.join(app.root_path, 'static', 'apk', 'forsaje.apk')
    return send_file(f, as_attachment=True, attachment_filename='taxi_forsaje.apk')
