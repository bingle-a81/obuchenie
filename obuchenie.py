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
n=int(input())
st = [list(map(int, input().split())) for i in range(n)]
r_matrix=[[[0] for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        r_matrix[j][n - i - 1] =  st[i][j]

# n=int(input())
# st = [list(map(int, input().split())) for i in range(n)]
# st.reverse()


for i in range(n):
    for j in range(n):
        print(r_matrix[i][j], end=" ")
    print()



# for i in range(n):
#     for j in range(n):
#         st[i][j], st[n - i - 1][i] = st[n - i - 1][i], st[i][j]
# print(('YES','NO')[a1])


# for i in range(n):
#     for j in range(n):
#         a: int=str(st[i][j]).rjust(2)
#         print(a, end=' ')
#     print()
