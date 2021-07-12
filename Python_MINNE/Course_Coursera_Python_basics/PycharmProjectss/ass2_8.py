n = int(input())
m = int(input())
k = int(input())

ss = n*m - 1

if k >= (m*n):
    print("NO")
elif k % n == 0 or k % m == 0:
    print("YES")
else:
    print("NO")
