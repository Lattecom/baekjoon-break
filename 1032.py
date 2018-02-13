# 1032
from sys import stdin as m
n=int(m.readline())
s=[]
for _ in range(n):
    s.append(m.readline())
l=len(s[0])
t=""
for i in range(l):
    c=s[0][i]
    f=1
    for j in range(n):
        if c!=s[j][i]:
            f=0
    t+=c if f else "?"
print(t)
