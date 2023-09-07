from sqlalchemy.orm import sessionmaker
from db import engine
from model import login, product, point_management
from sqlalchemy import text
SessionClass = sessionmaker(engine)  # セッションを作るクラスを作成
session = SessionClass()
connection = engine.connect()
#user_a = login(name="yanai", password="123")
#session.add(user_a)
#session.commit()

def selectAllLogin():
    users = session.query(login).all()
    return users

def getLoginUser(username, password):
    query = text(f'SELECT * FROM login WHERE name = "{username}" AND password="{password}"')
    result = connection.execute(query)
    row = result.fetchall()
    return row

def selectAllProduct():
    products = session.query(product).all() #mysqlから製品テーブルからデータを取得
    return products

def selectByIdProduct(productIdArr):
    if len(productIdArr) == 1:
        query = text(f'SELECT * FROM product WHERE id = {productIdArr[0]};')
    else:
        query = text(f'SELECT * FROM product WHERE id IN {tuple(productIdArr)};')
    result = connection.execute(query)
    row = [{"id": item.id,
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "quantity": 0
            } for item in result]
    return row

def pointodata(id):
    query = text(f'SELECT * FROM point_management WHERE user_id = "{id}";')
    result = connection.execute(query)
    row = result.fetchall()
    return row
