import math

used = [0]*2000000

def sanguocnhonhat() :
	global used
	for i in used :
		a[i] = i
	for i in range(2, int(math.sqrt(2000000))) :
		if a[i] == i :
			for j in range(i*i, 2000000) :
				a[j] = i


t = int(input())
sum = 0
while t > 0 :
