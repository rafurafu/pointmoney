#ログインプログラム
import csv

 #新規登録
def register():
    username = input("ユーザー名を入力してください: ")
    password = input("パスワードを入力してください: ")
 #ユーザー情報をファイルに登録 
    with open('users.csv', 'a',newline='') as file:
        writer = csv.writer(file)
        data = [username,password]
        writer.writerow(data)
        print("登録が完了しました。")

 #ログイン処理　、ユーザー情報の照合
def login():
    username = input("ユーザー名を入力してください: ")
    password = input("パスワードを入力してください: ")
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        #1行ずつCSVを読み込み
        line = [row for row in reader] 
        i = 0
        while True:  
            try:
                u_name = line[i][0]
                u_pass = line[i][1]
                if u_name == username and u_pass == password:
                    print("ログインに成功しました。")
                    return True
                i += 1
            except IndexError as e:
                print("ユーザー名またはパスワードが正しくありません。")
                return False
 #ログアウト                      
def logout():
    print('ログアウトしました')

 #表示プログラム
logged_in = False

while True:
    print("1. ログイン")
    print("2. ログアウト")
    print("3. 終了")
    print("4.新規登録")
    choice = input("選択肢を入力してください: ")

    if choice == "1":
        if logged_in:
            print("既にログイン済みです。")
        else:
            logged_in = login()
    elif choice == "2":
        if logged_in:
            logout()
            logged_in = False
        else:
            print("ログインしていません。")
    elif choice == "3":
        break
    elif choice == "4":
        register()
    else:
        print("無効な選択肢です。")
    
