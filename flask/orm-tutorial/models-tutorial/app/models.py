from app import db


class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(120), unique=False)
	last_name = db.Column(db.String(120), unique=False)
	company = db.Column(db.String(120), unique=False)
	email = db.Column(db.String(120))
	phone = db.Column(db.String(10))
	addresses = db.relationship('Address', backref='customer',
                                lazy='dynamic')
    # You need to a relationship to Address table here
    # see http://flask-sqlalchemy.pocoo.org/2.1/models/#one-to-many-relationships

	def __repr__(self):
		return '<Customer %r>' % self.email

# Your Address code should go here
# class Address(db.Model):
class Address(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	street_address = db.Column(db.String(120))
	city = db.Column(db.String(120), unique=False)
	state = db.Column(db.String(120), unique=False)
	country = db.Column(db.String(120), unique=False)
	zip_code = db.Column(db.String(10), unique=False)
	person_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

	def __repr__(self):
		return '<Address %r>' % street_address

class Order(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	total_spent = db.Column(db.String(120))
	num_parts_ordered = db.Column(db.String(120), unique=False)
