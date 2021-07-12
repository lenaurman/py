n = int(input())
a = n // 100
n = n - a*100
b = n // 10
c = n - b*10
print(a+b+c)
