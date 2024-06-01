countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[0:-3:1])

quit(-1)
n = 4
st: list[list[int]] = [[7, 12 ,1, 14], [2, 13 ,8 ,11], [16, 3, 10, 5], [9, 6, 15, 4]]
st2 = list(zip(*st))
s1: int = sum(st[0])
numbers: list[int] = [st[i][j] for j in range(n) for i in range(n)]
flag = True
if set(list(range(1, n * n + 1))) != set(numbers):
    flag = False

for i in range(n):
    if s1 != sum(st[i]) or s1 != sum(st2[i]):
        flag = False
        break
sum1 = 0
sum2 = 0
for i in range(n):
    for j in range(n):
        if i == n-j-1:
            sum2 += st[i][n - i - 1]
        if i == j:
            sum1 += st[i][j]
        # e=n-i-1
        # print(e)


if s1!=sum1 or s1!=sum2:
    flag = False

if flag:
    print("YES")
else:
    print("NO")


# for i in range(n):
#     if s1 != sum(st2[i]):
#         print("NO")
#         break

# for i in range(n):
#     for j in range(n):


# for i in range(n):
#     for j in range(n):
#         print(st[i][j], end=" ")
#     print()

# n = int(input())
# n:int = 4
# st: list[list[int]] = [list(map(int, input().split())) for i in range(n)]
# k,l=list(map(int,input().split()))
# print(k,l)

# l=int(input())

# n = 3
# st: list[list[int]] = [[1, 2, 3],
#                        [4, 5, 6],
#                          [7, 8, 9]]
# n = int(input())
# st = [list(map(int, input().split())) for i in range(n)]
# r_matrix = [[[0] for i in range(n)] for j in range(n)]

# for i in range(n):
#     for j in range(n):
#         r_matrix[j][n - i - 1] = st[i][j]

# n=int(input())
# st = [list(map(int, input().split())) for i in range(n)]
# st.reverse()


# for i in range(n):
#     for j in range(n):
#         print(r_matrix[i][j], end=" ")
#     print()


# for i in range(n):
#     for j in range(n):
#         st[i][j], st[n - i - 1][i] = st[n - i - 1][i], st[i][j]
# print(('YES','NO')[a1])


# for i in range(n):
#     for j in range(n):
#         a: int=str(st[i][j]).rjust(2)
#         print(a, end=' ')
#     print()
