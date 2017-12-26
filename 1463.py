# 1463
n = int(input())

x = [0, 0, 1, 1]

if n < 4:
	print(x[n])
else:
	for i in range(4, n+1):
		if i % 3 == 0 and i % 2 == 0:
			x.append(min(x[i-1], x[i//2], x[i//3]) + 1)
		elif i % 3 == 0:
			x.append(min(x[i-1], x[i//3]) + 1)
		elif i % 2 == 0:
			x.append(min(x[i-1], x[i//2]) + 1)
		else:
			x.append(x[i-1] + 1)

	print(x[i])