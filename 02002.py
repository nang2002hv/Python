fibo = [0]*100
fibo[1] = 1
for i in range(2,93) :
    fibo[i] = fibo[i-1] + fibo[i-2]
t = int(input())
while t > 0:
    x, y = [int(x) for x in input().split()]
    for i in range(x,y+1) :
        print(fibo[i], end =" ")
    print()
    t -= 1