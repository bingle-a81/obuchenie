from itertools import combinations

answers = [
    "2-й вариант предпочтительнее",
    "2-й вариант вполне допустим",
    "1-й предпочтительнее",
    "1-й вариант вполне допустим",
]
print(*combinations(sorted(answers), 2), sep="\n")
