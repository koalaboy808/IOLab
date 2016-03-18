from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm, AddressForm, OrderForm


@app.route('/')
def index():
    return redirect('/create_customer')

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    form = CustomerForm()
    address_form = AddressForm()
    order_form = OrderForm()
    if request.method == "POST":
        if form.validate_on_submit():
    # if request.form.get("action") == "add-customer":
            customer = models.Customer(
                                first_name = form.first_name.data,
                                last_name = form.last_name.data,
                                company = form.company.data,
                                email = form.email.data,
                                phone = form.phone.data
                                )
            # you will need to add Address here
            db.session.add(customer)
            db.session.commit()
            return redirect('/customers')
        elif address_form.validate_on_submit():
        # elif request.form.get("action") == "add-address":
            address = models.Address(
                                street_address = address_form.street_address.data,
                                city = address_form.city.data,
                                state = address_form.state.data,
                                country = address_form.country.data,
                                zip_code = address_form.zip_code.data
                                )
            # you will need to add Address here
            db.session.add(address)
            db.session.commit()
            return redirect('/customers')
        elif order_form.validate_on_submit():
        # elif request.form.get("action") == "add-address":
            order = models.Order(
                                total_spent = order_form.total_spent.data,
                                num_parts_ordered = order_form.num_parts_ordered.data
                                )
            # you will need to add Address here
            db.session.add(order)
            db.session.commit()
            return redirect('/customers')
    return render_template('customer.html', form=form, address_form=address_form, order_form=order_form)

@app.route('/customers')
def display_customer():
    customers = models.Customer.query.all()
    addresses = models.Address.query.all()
    orders    = models.Order.query.all()
    return render_template('home.html',
                            customers=customers,
                            addresses=addresses,
                            orders   =orders)
