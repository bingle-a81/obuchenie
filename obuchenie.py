# n = int(input())
n = 4
a1 = a2 = a3 = a4 = 0

# st = [list(map(int, input().split())) for i in range(n)]
st = [[1, 2, 3, 4], [5, 6, 7, 8], [3, 4, 5, 6], [1, 2, 3, 4]]

max = st[0][0]
for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            a1 += st[i][j]
        elif i < j and i > n - 1 - j:
            a2 += st[i][j]
        elif i > j and i > n - 1 - j:
            a3 += st[i][j]
        elif i > j and i < n - 1 - j:
            a4 += st[i][j]

print(
    f"""Верхняя четверть: {a1}
Правая четверть: {a2}
Нижняя четверть: {a3}
Левая четверть: {a4}"""
)
