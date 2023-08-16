from flask import Flask, render_template, request, url_for, redirect
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

class Order_Template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, nullable=True) 
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True)
    quantity = db.Column(db.Integer, nullable=False)
    #price = db.Column(db.Float, nullable=False) 

class Order_for_post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True)
    quantity = db.Column(db.Integer, nullable=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    postcode = db.Column(db.String(20), nullable=False)
    address_number = db.Column(db.String(10), nullable=False)

 
    # Add more fields as needed for order information


with app.app_context():
    db.create_all()


def create_order_entry(product_id, quantity):

    db.session.query(Order_Template).delete()
    db.session.commit()

    order_entry = Order_Template(product_id=product_id, quantity=quantity)

    db.session.add(order_entry)
    db.session.commit()

    





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
    fender_guitars = Product.query.filter_by(make = "Fender").all()
    return render_template('fenders.html', fender_guitars=fender_guitars)

@app.route('/gibson')
def gibson():
    gibson_guitars = Product.query.filter_by(make = "Gibson")
    return render_template('gibson.html', gibson_guitars=gibson_guitars)

@app.route('/cart')
def cart():
    orders = Order_Template.query.all()
    guitar_name = request.args.get('guitar_name')
    guitar_price = float(request.args.get('guitar_price'))
    quantity = int(request.args.get('quantity'))
    #product_id = int(request.args.get('product_id'))
    
    


    
    total_price = guitar_price * quantity
    

    return render_template('cart.html', orders=orders, guitar_name=guitar_name, guitar_price=guitar_price, total_price=total_price)

@app.route('/add-to-cart/<int:guitar_id>/<string:guitar_name>/<float:guitar_price>', methods=['GET', 'POST'])
def add_to_cart(guitar_id, guitar_name, guitar_price):
    quantity = int(request.form['quantity'])
    create_order_entry(guitar_id, quantity)
    return redirect(url_for('cart', guitar_name=guitar_name, guitar_price=guitar_price, quantity=quantity, product_id=guitar_id))


@app.route('/guitar/<int:guitar_id>')
def guitar_details(guitar_id):
    guitar = Product.query.get(guitar_id)
    return render_template('guitar_details.html', guitar=guitar)

@app.route('/payment', methods=['GET', 'POST'])
def payment(guitar_id, quantity):
    if request.method == "GET":
        return render_template('payment.html', quantity=quantity, product_id=guitar_id)

@app.route('/process_payment', methods=['POST', 'GET'])
def process_payment():
    if request.method == 'POST':
        # Extract form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        postcode = request.form['postcode']
        address_number = request.form['address_number']
        quantity = int(request.form['quantity'])
        product_id = int(request.args.get('product_id'))

        
        
        # Create a new customer entry in the Customer table
        new_customer = Customer(
            first_name=first_name,
            last_name=last_name,
            email=email,
            # ... other data fields ...
        )

        new_order = Order_for_post(

            first_name=first_name,
            last_name=last_name,
            postcode=postcode,
            address_number=address_number,
            quantity=quantity,
            product_id=product_id
        )
        
        # Add and commit the new customer to the database
        db.session.add(new_customer)
        db.session.commit()
        
        # Create a new order entry
        
        
        # Add and commit the new order to the database
        db.session.add(new_order)
        db.session.commit()
        
        # Redirect to the thank you page
        return redirect(url_for('thank_you'))


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')



# Add more routes for other pages as needed


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 5008)
