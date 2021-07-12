a, b, c = int(input()), int(input()), int(input())

if a > b or a > c:
    if b > c:
        (a, c) = (c, a)
    else:
        (a, b) = (b, a)

    if b > c:
        (b, c) = (c, b)

elif b > c:
    (b, c) = (c, b)

print(a, b, c)
