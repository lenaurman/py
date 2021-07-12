A = int(input())
B = int(input())

C = bool(A % B)
C = not C

D = C * 'YES' + (not C) * 'NO'
print(D)
