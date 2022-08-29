import math

def nt(n) :
	for i in range(2, int(math.sqrt(n))+1) :
		if n % i == 0 : return False
	return n > 1

def check(i) :
	if i == 2 or i == 3 or i == 5 or i == 7 :
		return True 
	return False

def kiemtra(n) :
	if(nt(len(n)) == False) : return False
	dem = 0
	for i in n:
		if(check(int(i))) : dem += 1
	if (dem > len(n)-dem) : return True
	return False
# mian	
t = int(input())
while t > 0 :
	n = input()
	if kiemtra(n) : print("YES")
	else : print("NO") 
	t -= 1