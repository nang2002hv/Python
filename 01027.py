dem = 0


def check(s):
    global dem
    dem += 1
    n = 0
    for i in s:
        n += int(i)
    if n >= 10:
        check(str(n))
    else:
        return 1


# main

s = input()
check(s)
print(dem)
