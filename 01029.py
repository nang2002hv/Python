import math

t = int(input())
while t > 0:
    n = input()
    m = n[::-1]
    if math.gcd(int(n), int(m)) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1
