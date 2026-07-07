# 演習7：総合応用：待ち時間シミュレーション
# arrival_times の6人について、1人あたり3分の体験として
# 各自の待ち時間を計算し、最長待ち時間を表示する

arrival_times = [0, 3, 4, 10, 11, 12]
play_time = 3

# TODO: 直前の人の終了時刻を管理する変数を用意する
pre_finish_time = 0


# TODO: 各来訪者の待ち時間を格納するリストを用意する
waiting_times = []


# TODO: ループで各来訪者の開始時刻・終了時刻・待ち時間を計算する
for arrival_time in arrival_times:
	waiting_times.append(pre_finish_time - arrival_time)
	if pre_finish_time <= arrival_time:
		pre_finish_time = play_time + arrival_time
	else:
		pre_finish_time += play_time


# TODO: 最長待ち時間を表示する
print(f"Max waiting time: {max(waiting_times)}")
