a =int(input())
b =int(input())
n =int(input())



s=a*n*60+b*n

print(s//3600,s%3600//60,s%60)
