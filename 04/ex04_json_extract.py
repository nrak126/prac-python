# 演習4：JSONからの特定データ抽出
# employee_data.json を読み込み、Sales部署の社員の名前と給与を表示する

import json

# TODO: employee_data.json を開いてJSONデータを読み込む
with open("employee_data.json", "r") as f:
    data = json.load(f)

# TODO: ループで社員データを走査し、department が "Sales" の社員だけ
#       name と salary を表示する
for d in data:
    if d["department"] == "Sales":
        print(f"name: {d["name"]}")
        print(f"salary: {d["salary"]}")
