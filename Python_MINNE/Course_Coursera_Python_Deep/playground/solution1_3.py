import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

x1 = (-1*b + math.sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-1*b - math.sqrt(b**2 - 4*a*c))/(2*a)

x1 = int(x1)
x2 = int(x2)

print(x1)
print(x2)
