from flask import Flask, render_template,request,redirect,session,jsonify
import session as ss
import json
import random
from model import product
from collections import Counter

app = Flask(__name__)
app.secret_key = 'your_secret_key'

 #ログインシステム
def login_required(func):
    def wrapper(*args, **kwargs):
        if 'username' in session:
            #ユーザーネームがある場合はhomeに移動
            return func(*args, **kwargs)
        else:
            #ユーザーネームがない場合はログイン画面に移動
            return redirect('/')
    return wrapper

 
 #ホーム
@app.route('/home')
@login_required
def index():
    id = session.get("id")
    pointKanri = ss.pointodata(id)
    if pointKanri:
        userPoint = pointKanri[0][2]
    else:
        userPoint = 0
    return render_template("home.html", point = userPoint)
 
 
 #ログイン
@app.route('/')
def login():
    return render_template("login.html")

@app.route('/login', methods = ["POST"])
def loginProcess():
    username = request.form["username"]
    password = request.form["password"]
    
    print(f"USername: {username}")
    print(f"Password:{password}")
    #username一時的に保存
    #username = セッション
    if loginCheck(username, password):
        return redirect("/home")

    else:
        return redirect("/")
    
 
 #ログアウト  
@app.route('/logout')
def logout():
    #ログアウトするときにセッションを消す
    session.clear()
    return redirect('/')
 
 
 #ログイン処理　、ユーザー情報の照合 #mysql
def loginCheck(username, password):
    users = ss.getLoginUser(username, password)
    
    if users[0][1] == username and users[0][2] == password:
        session['username'] = username
        session['id'] = users[0][0]
        return True
    else:
        return False


  #じゃんけん  
@app.route('/play_janken')
def play_janken():
    choices = {1: 'グー', 2: 'チョキ', 3: 'パー'}
    computer_choice = random.choice(list(choices.values()))
    user_choice = int(input("1: グー, 2: チョキ, 3: パー のいずれかを選んでください: "))
    
    if user_choice not in choices:
        # 無効な選択の場合、エラーメッセージを表示して終了
        print("無効な選択です。もう一度やり直してください。")
        return False
    
    # コンピューターの選択とユーザーの選択を表示
    print("コンピューターの選択:", computer_choice)
    print("あなたの選択:", choices[user_choice])
    
    if choices[user_choice] == computer_choice:
        # 引き分けの場合、メッセージを表示して終了
        print("引き分けです!")
        return False
    
    win_conditions = {
        'グー': 'チョキ',
        'チョキ': 'パー',
        'パー': 'グー'
    }
    
    if win_conditions[choices[user_choice]] == computer_choice:
        # ユーザーが勝った場合、勝利メッセージを表示してTrueを返す
        print("あなたの勝ちです!")
        
    print("コンピューターの勝ちです!")
    return render_template("jyanken.html")

def main():
    points = 0
    
    while True:
        print("現在のポイント:", points)
        result = play_janken()
        if result:
            points += 10
        else:
            points -= 10
        
        # もう一回プレイするかユーザーに尋ねる
        play_again = input("もう一度プレイしますか？ (y/n): ").lower()
        if play_again != 'y':
            break
    
    # 最終ポイントを表示して終了
    print("最終ポイント:", points)
    print("プレイしていただきありがとうございました！")
    
    
 
 #ポイント消費ページ          
@app.route('/shopping')
def shopping():
    username = session.get("username")
    if username:  
        product_list = ss.selectAllProduct()
        return render_template("shopping.html", data=product_list)
    else:
        return redirect('/')
    
@app.route('/cart')
def cart():
    username = session.get("username")
    if username:  
        cartList = session.get("productCartList")
        return render_template("cart.html", data=cartList)
    else:
        return redirect('/')
 
 
 #カートに追加
@app.route('/cart-proc', methods=["POST"])
def cartProc():
    data_received = request.get_json()
    productIdArr = data_received["productIdArr"]
    
    uniqueProductIdArr = list(set(productIdArr))
    cartProductData = ss.selectByIdProduct(uniqueProductIdArr)
    print(type(cartProductData))
    countQuantity = Counter(productIdArr)
    for pid, count in countQuantity.items():
        for i in range(len(cartProductData)):
            if cartProductData[i]["id"] == pid:
                cartProductData[i]["quantity"] = count
    print(cartProductData)
    session['productCartList'] = cartProductData
    response = {"message": "SUCCESS"}
    return jsonify(response)


if __name__ == '__main__':
    app.run()

