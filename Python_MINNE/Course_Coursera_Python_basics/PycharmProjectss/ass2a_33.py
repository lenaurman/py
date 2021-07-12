n = int(input())

l = n - (n // 10) * 10
l05678 = (l == 0 or l == 5 or l == 6 or l == 7 or l == 8 or l == 9)

if (10 < n < 20) or l05678:
    print(n, "korov")
elif l == 1:
    print(n, "korova")
else:
    print(n, "korovy")
