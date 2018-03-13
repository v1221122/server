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

@app.route('/wait')
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
    time = 5
    context = {
        'car': current_car,
        'time': request.cookies.get('user_phone'),
        'refresh': True
    }
    return render_template('wait.html', **context)


@app.route('/wait_page')
def wait_page():
    confirm = False
    time = request.args.get('time') - 1
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
    context = {
        'car': current_car,
        'time': time,
        'confirm': confirm,
        'refresh': True
    }
    return render_template('wait_page.html', **context)


@app.route('/cancel')
def cancel():
    with db_session:
        if request.cookies.get('user_phone'):
            Taxi_order.select(phone=request.cookies.get('user_phone')).delete(Bulk=True)
    return redirect('/')

@app.route('/application')
def application():
    f = os.path.join(app.root_path, 'static', 'apk', 'forsaje.apk')
    return send_file(f, as_attachment=True, attachment_filename='taxi_forsaje.apk')
