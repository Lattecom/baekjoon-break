# 1002
from sys import stdin
t = int(stdin.readline())

for _ in range(t):
	x1, y1, r1, x2, y2, r2 = map(int, stdin.readline().split(' '))
	a = (x1-x2)**2 + (y1-y2)**2
	r = (r1-r2)**2
	if a == 0 and r == 0 :
		print(-1)
	elif a == r:
		print(1)
	elif a < r:
		print(0)
	else:
		r = (r1+r2)**2
		if a > r:
			print(0)
		elif a == r:
			print(1)
		else:
			print(2)