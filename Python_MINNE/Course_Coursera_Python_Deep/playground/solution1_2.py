import sys

digit_string = sys.argv[1]

n = int(digit_string)
N = n

while n > 0:
    n -= 1
    empty = ' ' * n	
    str = '#' * (N - n)
    print(empty + str)
