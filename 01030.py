import math

a, b = [int(x) for x in input().split()]

dem = 0
for x in range(pow(10, b - 1), pow(10, b)):
    if math.gcd(a, x) == 1:
        dem += 1
        print(x, end=" ")
    if dem == 10:
        dem = 0
        print()
