# 1003

n = int(input())

l0 = [1, 0]
l1 = [0, 1]
for i in range(n):
	k = int(input())
	l = len(l0)-1
	if l < k:
		for j in range(l, k):
			l0.append(l0[j-1] + l0[j])
			l1.append(l1[j-1] + l1[j])

	print(l0[k],l1[k])