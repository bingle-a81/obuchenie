st = 's t e p i k r o c k s'.split()

a = [[]]

for i in range(len(st)):
    for j in range(len(st)):
        result = st[j:i + j + 1]
        if len(result) == i + 1:
            a.append(result)

print(a)
