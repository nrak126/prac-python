import json
import statistics


def calc_average(results: list) -> float:
    return statistics.mean([r.get('score') for r in results])



def find_top_scorer(results: list) -> dict:
    return max([r.get('score') for r in results])


with open("exam_results.json", "r") as f:
    data = json.load(f)

# TODO: calc_average を呼び出して平均点を表示する
print(calc_average(data))

# TODO: find_top_scorer を呼び出して最高得点者の名前と点数を表示する
print(find_top_scorer(data))
