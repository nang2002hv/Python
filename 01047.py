import math


def nguyento(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True


t = int(input())
while t > 0:
    s = input();
    if nguyento(int(s[-4::])):
        print("YES")
    else:
        print("NO")
    t -= 1
