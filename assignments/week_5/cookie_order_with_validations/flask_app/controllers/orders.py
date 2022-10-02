from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.order import Order

@app.route('/')
def index():
    return redirect('/cookies')

@app.route('/cookies')
def cookies():
    return render_template("cookies.html", all_orders = Order.get_all_orders())

@app.route('/cookies/edit/<int:id>')
def edit_cookies(id):
    # order = Order.get_order_by_id(id)
    return render_template("edit-order.html", order = Order.get_order_by_id(id))

@app.route('/update/order', methods=['POST'])
def update_order():
    if not Order.validate_order(request.form):
        return redirect(f"/cookies/edit/{request.form['id']}")
    print(request.form)
    Order.update_order(request.form)
    return redirect ('/')

@app.route('/cookies/new/')
def new_order():
    return render_template('new-order.html')

@app.route('/create/order', methods=['POST'])
def add_order():
    if not Order.validate_order(request.form):
        return redirect(f"/cookies/new")
    print(request.form)
    Order.new_order(request.form)
    return redirect ('/')
