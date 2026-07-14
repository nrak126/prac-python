import math

# お題：円の面積を計算する関数
# ライターの仕様書に従って、計算処理を実装してください。
def calc_circle_area(radius):
    return math.pi * radius ** 2


# テスト例
assert calc_circle_area(3) == 28.274333882308138
assert calc_circle_area(5) == 78.53981633974483
assert calc_circle_area(10) == 314.1592653589793

print("すべてのテストをクリアしました！")
