t = int(input())
while t > 0:
    a = list(input())
    a.sort()
    s = ""
    sum = 0
    for i in a:
        if i.isdigit():
            sum += int(i)
        else:
            s += i
    print(s + str(sum))
    t -= 1
