# 発展課題: データの選別
#
# 以下の4つのステップを1つのプログラムで実装してください。
#
#   1. 整数乱数を 100個 生成し、リストに格納する
#   2. バブルソート を自作してリストを昇順に並び替える
#   3. 上位 50個 のみを抽出して新しいリストを作る
#   4. 抽出した中からランダムに 2個 を選び表示する

import random

# ステップ1: 整数乱数を100個生成してリストに格納
# TODO: random.randint() を使って 1〜100 の整数を 100 個生成する
arr = [random.randint(1, 100) for i in range(100)]

# ステップ2: バブルソートでリストを昇順に並び替える
# TODO: 2重ループで隣り合う要素を比較・入れ替えする
for i in range(arr.__len__()):
	for j in range(arr.__len__() - i - 1):
		if arr[j + 1] < arr[j]:
			arr[j], arr[j + 1] = arr[j + 1], arr[j]

# ステップ3: 上位50個を抽出して新しいリストを作る
# TODO: ソート済み data の後半50個をスライスで取り出す
sliced_arr = arr[50:100]

# ステップ4: 抽出した中からランダムに2個を選び表示する
# TODO: random.sample() を使って top50 から2個選ぶ
print(random.sample(sliced_arr, 2))
