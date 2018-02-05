x = int(input())
i = 1
while True:
	if x > (i * (i+1) / 2):
		i += 1
	else:
		break

x = int((x-(i*(i-1)/2)) -1)
a, b = (i-x, 1+x) if i % 2 == 1 else (1+x, i-x)
print(str(a)+'/'+str(b))