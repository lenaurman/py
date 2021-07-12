N = int(input())
i = N
min_i = i

while i > 1:
    if N % i == 0:
        min_i = i
    i = i - 1

print(min_i)
