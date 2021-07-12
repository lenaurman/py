x = int(input())
p = x
n = 0
while x != 0:
    x = int(input())
    if x > p:
        n = n + 1
    p = x

print(n)
