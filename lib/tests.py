from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base,Customer, Review, Restaurant

engine = create_engine('sqlite:///restaurants.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

print("Full names")

all_customer=session.query(Customer).all()
for customer in all_customer:
    print(customer.first_name, customer.last_name)

print("restuarant name")

all_restaurant=session.query(Restaurant).limit(1)
for restaurant in all_restaurant:
  print(restaurant.name, restaurant.price)
  
  #get reviews
target_restaurant_name = "Tasty Bites"
target_restaurant = session.query(Restaurant).filter_by(name=target_restaurant_name).first()

if target_restaurant:
    print(f"Reviews for {target_restaurant_name}:")
    for review in target_restaurant.reviews:
        print(f"{review.customer.full_name()}: {review.star_rating} stars")
else:
    print(f"Restaurant '{target_restaurant_name}' not found.")

#Get Reviews from a specific Customer
target_customer_name = "John Doe"
target_customer = session.query(Customer).filter_by(full_name=target_customer_name).first()

if target_customer:
    print(f"Reviews given by {target_customer_name}:")
    for review in target_customer.reviews:
        print(f"{review.restaurant.name}: {review.star_rating} stars")
else:
    print(f"Customer '{target_customer_name}' not found.")
    
# Add Reviews
target_restaurant_name = "Spicy Haven"
target_restaurant = session.query(Restaurant).filter_by(name=target_restaurant_name).first()

if target_restaurant:
    john_doe = session.query(Customer).filter_by(full_name="John Doe").first()
    print(f"Review added by {john_doe.full_name()} for {target_restaurant_name}.")
else:
    print(f"Restaurant '{target_restaurant_name}' not found.")


