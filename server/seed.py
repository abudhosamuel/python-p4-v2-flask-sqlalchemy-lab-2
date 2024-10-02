#!/usr/bin/env python3

from app import app
from models import db, Customer, Review, Item

with app.app_context():
    # Clear any existing data in the tables (ensure the right order due to foreign key constraints)
    Review.query.delete()
    Customer.query.delete()
    Item.query.delete()

    # Create sample customers
    customer1 = Customer(name='Tal Yuri')
    customer2 = Customer(name='Raha Rosario')
    customer3 = Customer(name='Luca Mahan')
    db.session.add_all([customer1, customer2, customer3])
    db.session.commit()  # Commit customers first to assign them IDs

    # Create sample items
    item1 = Item(name='Laptop Backpack', price=49.99)
    item2 = Item(name='Insulated Coffee Mug', price=9.99)
    item3 = Item(name='6 Foot HDMI Cable', price=12.99)
    db.session.add_all([item1, item2, item3])
    db.session.commit()  # Commit items next to assign them IDs

    # Create reviews and associate them with customers and items
    review1 = Review(comment="Zipper broke the first week", customer=customer1, item=item1)
    review2 = Review(comment="Love this backpack!", customer=customer2, item=item1)
    review3 = Review(comment="Coffee stays hot for hours!", customer=customer1, item=item2)
    review4 = Review(comment="Best coffee mug ever!", customer=customer3, item=item2)
    review5 = Review(comment="Cable too short", customer=customer3, item=item3)
    
    # Add the reviews to the session and commit
    db.session.add_all([review1, review2, review3, review4, review5])
    db.session.commit()

    print("Database successfully seeded with customers, items, and reviews!")
