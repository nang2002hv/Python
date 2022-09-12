t = int(input())
while t > 0:
    s = input()
    sum = 0;
    res = 1;
    for i in range(len(s)):
        if i % 2 == 0 and int(s[i]) != 0:
            res *= int(s[i])
        else:
            sum += int(s[i])
    print(res, sum, sep=" ")
    t -= 1
