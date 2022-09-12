t = int(input())

while t > 0:
    s = input()
    sum = 0
    res = 1
    ok = True
    for i in range(len(s)):
        if i % 2 == 0:
            sum += int(s[i])
        else:
            if (int(s[i]) != 0):
                ok = False
                res *= int(s[i])
    print(sum, end=" ")
    if ok == False:
        print(res)
    else:
        print("0")
    t -= 1
