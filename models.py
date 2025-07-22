from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Orders(Base):
    __tablename__ = 'orders' 

    id = Column(Integer, primary_key=True, autoincrement=True)
    Product = Column(String(100))  
    Quantity = Column(Integer)
    Price = Column(Float)

    def __init__(self, Product, Quantity, Price): 
        self.Product = Product
        self.Quantity = Quantity
        self.Price = Price
   