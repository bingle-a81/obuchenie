from decimal import *

num = Decimal(input())

a=num.as_tuple()

if len(a[1])/(-1*a[2])==1:
    print(max(a[1]))
else:
    print(max(a[1])+min(a[1]))
