t = int(input())

while t > 0 :
	s = input()
	a = s[0 : 3]
	b = s[len(s) -3 : len(s)]
	print(b)
	t -= 1