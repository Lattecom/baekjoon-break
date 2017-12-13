# 2448

def buildTri(tree):
	newTree = ""
	origin = TRI.split("\n")
	length = len(origin)

	for x in range(length):
		newTree += spaceN(length) + origin[x] + spaceN(length) + "\n"

	for i in range(length):
		line = origin[i] + spaceN(1) + origin[i] + "\n"
		newTree = newTree + line

	return newTree[:-1]

def spaceN(n):
	return " "*n

def root2(n):
	count = 0
	while n>1:
		n /= 2
		count += 1
		
	return count

TRI = "  *  \n * * \n*****"
n = input()

n = int(n)/3
n = root2(n)

for i in range(int(n)):
	TRI = buildTri(TRI)

print(TRI)
