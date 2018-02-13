# 1057

n,k,l=map(int,input().split())
x=y=0
while x==y:
	c=1
	x=y=0
	while k>c or l>c:
		if k>c: x+=1
		if l>c: y+=1
		c*=2	
	n=2**(x-1)
	k-=n
	l-=n
print(max(x,y))