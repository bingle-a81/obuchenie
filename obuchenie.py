n = int(input())
d = {}
for i in range(n):
    a, *b = input().split()
    d[a] = b

j = int(input())
for i in range(j):
    s = input()
    for k, v in d.items():
        if s in v:
            print(k)
            break
