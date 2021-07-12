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

if (A1 == A2) and (B1 == B2) and (C1 == C2):
    print("Boxes are equal")
elif (A1 <= A2) and (B1 <= B2) and (C1 <= C2):
    print("The first box is smaller than the second one")
elif (A1 >= A2) and (B1 >= B2) and (C1 >= C2):
    print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")



V1 = int(int(A1/A2) * int(B1/B2) * int(C1/C2))
V2 = int(int(A1/A2) * int(B1/C2) * int(C1/B2))
V3 = int(int(A1/B2) * int(B1/A2) * int(C1/C2))
V4 = int(int(A1/B2) * int(B1/C2) * int(C1/B2))
V5 = int(int(A1/C2) * int(B1/A2) * int(C1/C2))
V6 = int(int(A1/C2) * int(B1/C2) * int(C1/B2))