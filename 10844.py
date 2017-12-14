# 10844

n = int(input())

prev = []
post = [0, 1, 1, 1, 1,  1, 1, 1, 1, 1]
for i in range(n):
	prev = post.copy()
	post[0] = prev[1]
	for i in range(1,9):
		post[i] = prev[i-1] + prev[i+1]
	post[9] = prev[8]

print(sum(prev)%1000000000)
