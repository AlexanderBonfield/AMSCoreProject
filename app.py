from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt

app = Flask(__name__)

db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "projectdatabase.db")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path


app.config['SECRET_KEY']='Basta'
db = SQLAlchemy(app)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    # Add more fields as needed for customer information

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    make = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(300), nullable=True)

    # Add more fields as needed for product information

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    postcode = db.Column(db.String(100), nullable = False)
    house_number = db.Column (db.Integer, nullable=False) 
    # Add more fields as needed for order information


with app.app_context():
    db.create_all()




# Route for the home page
@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contactus.html')

@app.route('/fenders')
def fenders():
    fender_guitars = Product.query.filter_by(make = "fender").all()
    return render_template('fenders.html', fender_guitars=fender_guitars)

@app.route('/gibson')
def gibson():
    return render_template('gibson.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')


# Add more routes for other pages as needed


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 5008)
