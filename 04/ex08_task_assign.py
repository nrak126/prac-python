# 演習8：総合応用：タスク割り当て
# 9つの工芸品を部員3人で分担し、すべての製作が終了する日を表示する

work_days = [4, 1, 3, 1, 3, 4, 2, 4, 3]

# TODO: 部員3人の次に作業開始できる日を管理するリストを用意する（初期値は全員1日目）
day = [0, 0, 0]


# TODO: work_days をループし、各工芸品を「最も早く手が空く部員」に割り当てる
#       - 最も早く手が空く部員のインデックスを求める
#       - その部員の次の作業開始日を「現在の開始日 + 製作日数」に更新する

# for work in work_days:
#     index = day.index(min(day))
#     day[index] += work
    
# print(day)
# print(max(day))    

index = 0
for work in work_days:
    min = 10
    for i in range(len(day)):
       if min > day[i]:
           min = day[i]
           index = i
    
    day[index] += work
    
    print(day)

print(day)
print(max(day))   

 
    

# TODO: すべての製作が終了する日（全部員の最大値）を表示する
