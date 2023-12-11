# tests.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review  

# Create engine and bind it to the Base
engine = create_engine('sqlite:///restaurants.db', echo=True)
Base.metadata.bind = engine

#Restaurant CRUD

Session = sessionmaker(bind=engine)
session = Session()

# Example 1: Accessing reviews for a restaurant
restaurant_reviews = session.query(Restaurant).first().all_reviews()
print("Reviews for the first restaurant:")
print(restaurant_reviews)

# Example 2: Accessing restaurants for a customer
customer_restaurants = session.query(Customer).first().restaurants()
print("Restaurants reviewed by the first customer:")
print(customer_restaurants)

# Example 3: Finding the fanciest restaurant
fanciest_restaurant = Restaurant.fanciest()
print("Fanciest restaurant:")
print(fanciest_restaurant.name)

# Example 4: Adding a review for a customer
customer_to_review = session.query(Customer).first()
restaurant_to_review = session.query(Restaurant).first()
customer_to_review.add_review(restaurant_to_review, rating=4)

# Example 5: Deleting reviews for a restaurant
customer_with_reviews = session.query(Customer).first()
restaurant_to_delete_reviews = session.query(Restaurant).first()
customer_with_reviews.delete_reviews(restaurant_to_delete_reviews)

# ... add more examples as needed

# Commit changes
session.commit()
