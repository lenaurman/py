y = int(input())

if (y % 4 == 0 and (not(y % 100 == 0))) or y % 400 == 0:
    print("YES")
else:
    print("NO")