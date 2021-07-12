a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a + b + c + d) % 2 == 0 and d > b and a - (d - b) <= c <= a + (d - b):
    print('YES')
else:
    print('NO')
