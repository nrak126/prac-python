# 演習6：デバッグ（バグ修正）
# 以下のプログラムには意図した動作にならないバグが含まれている。
# 60点以上の点数だけの平均を正しく計算できるよう修正してください。

# TODO: このままだとエラーになる場合がある。原因を考えて修正する
import random

scores = [random.randint(0, 100) for i in range(10)]
print("生成された点数:", scores)

total = 0
count = 0
for s in scores:
    if s >= 60:
        total += s
    count += 1
        
average = total / count 
print("60点以上の平均点:", average)
