# 問題3: 平均値計算
# リストにある全ての数値の平均値を求めて表示する。
# Average = Total Sum / Count

numbers = [12, 45, 7, 23, 56, 19]

# TODO: 平均値を計算して表示する
sum = 0
for n in numbers:
	sum += n
print(sum / numbers.__len__())
