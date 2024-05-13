n=int(input())
a=0
st=[list(map(int,input().split())) for i in range(n)]

for i in range(n):
    for j in range(n):
        if i==j:
            a+=st[i][j]

print(a)