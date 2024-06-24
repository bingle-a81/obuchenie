import random
ls=[]
while len(ls)<100:
    for i in range(100):
        a=random.randrange(1_000_010, 10_000_000)

        if  a not in ls:
            ls.append(a)

print(*ls, sep="\n")
