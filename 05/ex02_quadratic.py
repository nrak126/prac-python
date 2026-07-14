import math

# ==========================================
# 【プログラマーが実装する部分（TODO）】
# ==========================================
# お題：二次方程式 ax^2 + bx + c = 0 の解を計算する関数
def calc_quadratic_equation(a, b, c):
    # TODO: 判別式 (D = b^2 - 4ac) を使って条件分岐を実装してください。
    # 虚数解は解なしとする    
    d = b ** 2 - 4 * a * c
    if d == 0:
        return (-b + d ** 0.5) / (2 * a)
    if d < 0:
        return "解なし"
    if d > 0:
        return ((-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a))


# テスト例①：解が2つある場合 (x^2 - 4 = 0)
assert calc_quadratic_equation(1, 0, -4) == (2.0, -2.0)

# テスト例②：重解の場合 (x^2 - 2x + 1 = 0)
assert calc_quadratic_equation(1, -2, 1) == 1.0

# テスト例③：虚数解の場合 (x^2 + 4 = 0)
assert calc_quadratic_equation(1, 0, 4) == "解なし"

print("すべてのテストをクリアしました！")
