# 演習5：JSONデータの特定条件集計
# product_data.json を読み込み、在庫が10個未満の商品名と在庫合計を表示する

import json

# TODO: product_data.json を開いてJSONデータを読み込む
with open("product_data.json", "r") as f:
    data = json.load(f)

# TODO: 在庫(stock)が10個未満の商品を抽出し、商品名を表示する
#       同時に在庫合計を計算する
print(f"在庫が10以下の商品一覧")
sum = 0
for d in data:
  if d["stock"] < 10:
    print(d["name"])
    sum += d["stock"]

# TODO: 在庫合計を表示する
print(f"在庫合計: {sum}")