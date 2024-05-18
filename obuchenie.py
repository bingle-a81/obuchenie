# n = int(input())
# n:int = 4
# st: list[list[int]] = [list(map(int, input().split())) for i in range(n)]
# k,l=list(map(int,input().split()))
# print(k,l)

# l=int(input())




n:int = 3
# m=4
# k=0
# l=2
st: list[list[int]] = [[1, 2, 3],
                        [2, 6, 7],
                          [3,7,11]]
a1=False
for i in range(n):
    for j in range(n):
        if st[i][j]!=st[j][i]:
            a1=True
            break
        else:
            continue
    if a1:
        break


print(('YES','NO')[a1])




# for i in range(n):
#     for j in range(n):
#         a: int=str(st[i][j]).rjust(2)
#         print(a, end=' ')
#     print()

        

