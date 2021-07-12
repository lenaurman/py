N = int(input())
sum = 0
n = 1

while (n <= N):
    sum += 1 / n ** 2
    n += 1

if sum == round(sum):
    print(int(sum))
else:
    print(round(sum, ndigits=5))
