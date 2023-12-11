from sqlalchemy import Column, Text, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer(), primary_key=True)
    star_rating = Column(Integer())
    customer_id = Column(Integer, ForeignKey("customers.id"))
    restaurant_id = Column(Integer(), ForeignKey("restaurants.id"))
    
    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews')
    
    def customer(self):
        return self.customer
    
    def restaurant(self):
        return self.restaurant
    
    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."

class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())
    
    reviews = relationship('Review', back_populates='restaurant')
    
    def get_reviews(self):
        return self.reviews
   
    def customers(self):
        return [review.customer for review in self.reviews]
    
    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(cls.price.desc()).first()
     
    def all_reviews(self):
        return [review.full_review() for review in self.reviews]

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
   
    reviews = relationship("Review", back_populates='customer')
   
    def get_reviews(self):
        return self.reviews
   
    def restaurants(self):
        return [review.restaurant for review in self.reviews]
   
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
   
    def favorite_restaurant(self):
        return max(self.reviews, key=lambda review: review.star_rating).restaurant
     
    def add_review(self, restaurant, rating):
        new_review = Review(customer=self, restaurant=restaurant, star_rating=rating)
        session.add(new_review)
        session.commit()
        
    def delete_reviews(self, restaurant):
        for review in self.reviews:
            if review.restaurant == restaurant:
                session.delete(review)
        session.commit()
