from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Customer, Review, Restaurant

# Create engine and bind it to the Base
engine = create_engine('sqlite:///restaurants.db', echo=True)
Base.metadata.create_all(engine)

# Create a Session
Session = sessionmaker(bind=engine)
session = Session()


# Sample Restaurants
restaurant1 = Restaurant(name="Tasty Bites", price=3)
restaurant2 = Restaurant(name="Gourmet Delight", price=4)
restaurant3 = Restaurant(name="Spicy Haven", price=2)

# Sample Customers
customer1 = Customer(first_name="John", last_name="Doe")
customer2 = Customer(first_name="Jane", last_name="Smith")
customer3 = Customer(first_name="Bob", last_name="Johnson")

# Sample Reviews
review1 = Review(star_rating=5, customer=customer1, restaurant=restaurant1)
review2 = Review(star_rating=4, customer=customer2, restaurant=restaurant1)
review3 = Review(star_rating=3, customer=customer3, restaurant=restaurant2)
review4 = Review(star_rating=5, customer=customer1, restaurant=restaurant2)
review5 = Review(star_rating=2, customer=customer2, restaurant=restaurant3)

session.add_all([restaurant1, restaurant2, restaurant3, customer1, customer2, customer3, review1, review2, review3, review4, review5])
session.commit()
