A = int(input())
B = int(input())
C = int(input())

if A > B and A > C:
    D = A
elif B > C:
    D = B
else:
    D = C

print(D)
