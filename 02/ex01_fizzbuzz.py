# 問題1: フィズバズ
# 1から15までを繰り返し表示する。
# 3の倍数 → "Fizz"、5の倍数 → "Buzz"、両方 → "FizzBuzz"

for i in range(1, 16):
    print(i, end=": ")
    # TODO: 条件分岐を書く
    if i % 3 == 0:
        print("Fizz", end="")
    if i % 5 == 0:
        print("Buzz", end="")
    print()
    pass
