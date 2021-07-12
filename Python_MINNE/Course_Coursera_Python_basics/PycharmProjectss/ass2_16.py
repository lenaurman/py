A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
s1 = A * B
s2 = A * C
s3 = C * B
s4 = D * E

f1 = (s1 <= s4)
f2 = (s2 <= s4)
f3 = (s3 <= s4)
ff1 = ((A <= D) and (B <= E))
ff2 = ((A <= D) and (A <= E))
ff3 = ((A <= D) and (C <= E))
ff4 = ((C <= D) and (A <= E))
ff5 = ((B <= D) and (C <= E))
ff6 = ((C <= D) and (B <= E))

if (f1 or f2 or f3) and (ff1 or ff2 or ff3 or ff4 or ff5 or ff6):
    print('YES')
else:
    print('NO')
