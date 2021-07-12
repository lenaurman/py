h = int(input())
a = int(input())
b = int(input())

d = 1
h = h - a
print(d, h)

d = d + h / (a - b)
print(d)

if h % a > 0:
    d = d + 1

d = int(d)
print(d)
