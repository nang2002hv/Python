t = int(input())
while t > 0:
    k = 1
    s = input()
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            k += 1
        else:
            print(k, end="")
            print(s[i - 1], end="")
            k = 1
    print(k, end="")
    print(s[len(s) - 1], end="")
    print()
    t -= 1
