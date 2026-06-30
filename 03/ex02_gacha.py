import random

count = 0

for i in range(100):
    # pass  # TODO: 3% の確率で SSR が出たとき count を増やす
	if random.random() < 0.03:
		count += 1

print(f"SSRが出た回数: {count}")
