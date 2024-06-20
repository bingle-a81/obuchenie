def find_delitel(x:int):
    s=[]
    for i in range(1,x+1):
        if x%i==0:
            s.append(i)
    return s
numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
result = {x:find_delitel(x) for x in numbers}
print(result)