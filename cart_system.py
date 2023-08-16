
from app import db


def create_order_entry(product_id, quantity):

    order_entry = Order(product_id=product_id, quantity=quantity)

    db.session.add(cart_entry)
    db.session.commit()

