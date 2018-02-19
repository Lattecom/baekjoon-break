#1157
s=input().upper()
a={x:0 for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
for i in a.keys():
    a[i]+= s.count(i)
l=sorted(a.values())
m=max(l)
if m==l[-2]:
    c="?"
else:
    for k, v in a.items():
        if v==m:
            c=k
print(c)
