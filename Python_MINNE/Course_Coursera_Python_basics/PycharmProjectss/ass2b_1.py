N = int(input())
i = N
min_i = i

while i <= 2:
    if N % i == 0:
        min_i = i

print(min_i)
