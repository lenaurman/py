n = int(input())
n = n % (24*60)
h = n // 60
m = n - h*60
print(h, m)
