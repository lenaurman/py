A1, B1, C1 = int(input()), int(input()), int(input())
A2, B2, C2 = int(input()), int(input()), int(input())

if A1 > B1:
    (A1, B1) = (B1, A1)
if B1 > C1:
    (B1, C1) = (C1, B1)
if A1 > B1:
    (A1, B1) = (B1, A1)

if A2 > B2:
    (A2, B2) = (B2, A2)
if B2 > C2:
    (B2, C2) = (C2, B2)
if A2 > B2:
    (A2, B2) = (B2, A2)

V1 = ((A1//A2) * (B1//B2) * (C1//C2))
V2 = ((A1//A2) * (B1//C2) * (C1//B2))
V3 = ((A1//B2) * (B1//A2) * (C1//C2))
V4 = ((A1//B2) * (B1//C2) * (C1//A2))
V5 = ((A1//C2) * (B1//A2) * (C1//B2))
V6 = ((A1//C2) * (B1//B2) * (C1//A2))

print(max(V1, V2, V3, V4, V5, V6))
