h = int(input())
a = int(input())
b = int(input())

ff = 1 + ((h - a) // (a - b)) + (((h - a) % (a - b)) > 0)
print(ff)
