s=input()

d1={}
for x in s:
    d1.setdefault(x,0)
    d1[x]+=1

n=int(input())
d={}
for i in range(n):
    a,b=input().split(':')
    d[int(b)]=a

ls=[]
for i in s:
    ls.append(d.get(d1.get(i)))

print(*ls,sep='')








