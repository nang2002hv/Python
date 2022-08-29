import math

def nt(n) :
	for i in range(2, int(math.sqrt(n))+1) :
		if n % i == 0 : return False
	return n > 1
#main
t = int(input())
while t > 0 :
	n = input()
	s = 0
	for i in n :
		s += int(i)
	if(nt(s)) : print("YES")
	else : print("NO") 
	t -= 1