s1 = int(input())
s2 = int(input())
t1 = int(input())
t2 = int(input())

ss = t1 - s1
tt = t2 - s2

if ss % 2 == 0 and tt % 2 == 0:
    print("YES")
elif ss % 2 == 0 or tt % 2 == 0:
    print("NO")
else:
    print("YES")
