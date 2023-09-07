from typing import Any
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, BLOB
 #ログインデータ
class login(Base):
    __tablename__ = "login"  # テーブル名を指定
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    password = Column(String(256))
  
  #ショップデータ  
class product(Base):
    __tablename__ = "product" 
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    image = Column(BLOB)
    description = Column(String(200))
    price = Column(Integer)
    quantity = 0
    
    def __init__(self, id, name, image, description, price,quantity):
        self.id = id
        self.name = name
        self.image = image
        self.description = description
        self.price = price
        self.quantity = quantity
    
  #所有ポイント  
class point_management(Base):
    __tablename__ = "point_management"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    user_point = Column(Integer)
    
