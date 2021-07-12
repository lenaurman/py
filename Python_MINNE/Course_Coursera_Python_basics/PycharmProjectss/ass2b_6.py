a, b, c = int(input()), int(input()), int(input())
n = 0
if a == b:
    n = n + 2
    if b == c:
        n = n + 1
elif a == c:
    n = 2
elif b == c:
    n = 2

print(n)
