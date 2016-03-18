from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm, AddressForm


@app.route('/')
def index():
    return redirect('/create_customer')

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    form = CustomerForm()
    address_form = AddressForm()
    if request.method == "POST":
        # if form.validate_on_submit():
        if request.form.get("action") == "add-customer":
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
                                street = form.street_address.data,
                                city = form.city.data,
                                state = form.state.data,
                                country = form.country.data,
                                zip_code = form.zip_code.data
                                )
            # you will need to add Address here
            db.session.add(address)
            db.session.commit()
            return redirect('/customers')
    return render_template('customer.html', form=form)

@app.route('/customers')
def display_customer():
    customers = models.Customer.query.all()
    return render_template('home.html',
                            customers=customers)
