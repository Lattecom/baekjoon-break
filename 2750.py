# python 3
n = int(input())
a = list()
for i in range(n):
    a.append(int(input()))

def selectSort(a):
	for i in range(len(a)):
		min = 999999999999999
		minIndex = 0
		for j in range(i, len(a)):
			if a[j] < min:
				min = a[j]
				minIndex = j
		temp = a[i]
		a[i] = a[minIndex]
		a[minIndex] = temp
	return a

a = selectSort(a)

for i in a:
	print(i)