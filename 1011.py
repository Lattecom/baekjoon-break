# 1011
from sys import stdin
class Test():
	s = list("4\n0 3\n1 5\n45 50\n0 2000000000".split("\n"))
	c = -1

	def readline():
		Test.c += 1
		return Test.s[Test.c]

def main(inputInterface):

	N = int(inputInterface.readline())
	for i in range(N):
		x, y = map(int, inputInterface.readline().split())
		d = y - x
		k = 1

		while True:
			if d < 1 + k**2 - k:
				break
			k+=1

		k-=1
		
		if d >= 1 + k**2:
			print(k*2)
		else:
			print(k*2-1)

main(Test)