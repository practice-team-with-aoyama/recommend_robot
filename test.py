import csv
import os

lists =[]

# 最初の質問
print("こんにちは。あなたのお名前は？：",end="")
user_name = input()

# お勧めのレストランを質問
# print("name:{}　レストラン名を入力：".format(user_name),end="")
# restaurant_name = input()

# 初回起動か否かを確認
if not os.path.exists("test_csv.csv"):
    # 最初の質問
    print("name:{}　レストラン名を入力：".format(user_name),end="")
    restaurant_name = input()

    # listsにレストランを追加（list型）
    new_restaurant = [restaurant_name,0]
    lists.append(new_restaurant)

    # csvファイルに書き込み
    with open("test_csv.csv","w") as f:
            writer = csv.writer(f)
            for list in lists:
                writer.writerow(list)

else:
    # リコメンドを提示
    print("お勧めは◯◯です")
    print("このレストランはお好きですか？[Yes/No]")
    answer = input()

    while answer=="No":
        # リコメンドを提示
        print("お勧めは◯◯です")
        print("このレストランはお好きですか？[Yes/No]")
        answer = input()

    # Yes!
    # ↓↓↓↓

    # お勧めのレストランを質問
    print("name:{}　レストラン名を入力：".format(user_name),end="")
    restaurant_name = input()

    # csvファイルを読み込み
    with open("test_csv.csv","r+") as f:
        reader = csv.reader(f)
        for row_data in reader:
            # restaurant = Restaurant(row_data[0],row_data[1])
            lists.append(row_data)

        # 入力したレストランをリストに追加
        new_restaurant = [restaurant_name,0]
        lists.append(new_restaurant)

        # seek()を先頭に戻す
        f.seek(0)

        # csvファイルに再書き込み
        writer = csv.writer(f)
        for list in lists:
            writer.writerow(list)

# 終了処理
print("正常に終了")
