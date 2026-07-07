# 演習3：段階的割引の団体料金計算関数
# 人数に応じて段階的に料金が変わる calc_group_fee(visitors) を作成する
# 1〜20人目: 1000円/人、21〜50人目: 800円/人、51人目以降: 700円/人

# TODO: calc_group_fee(visitors) 関数を定義する
#       - 人数に応じた合計金額を計算して return する
def calc_group_fee(visitors: int) -> int:
	fee = 0
	if(visitors <= 20):
		fee += 1000 * visitors
		return fee
	
	fee += 1000 * 20
	if(visitors <= 50):
		fee += 800 * (visitors - 20)
		return fee
	
	fee += 800 * 30
	fee += 700 * (visitors - 50)
	return fee



# TODO: 人数が 15、35、60 の場合でそれぞれ関数を呼び出し、結果を表示する
print(calc_group_fee(15))
print(calc_group_fee(35))
print(calc_group_fee(60))