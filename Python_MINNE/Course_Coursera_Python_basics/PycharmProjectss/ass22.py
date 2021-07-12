n = int(input())

ff1 = ((n // 1000) == (n % 10))

n = n - (n // 1000) * 1000
n = n // 10
ff2 = ((n // 10) == (n % 10))

ff = (ff1 & ff2) * 1
print(ff)
