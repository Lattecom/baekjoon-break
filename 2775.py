# 2775
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    sum = 1
    for i in range(k+1):
        sum*=(n+i)
        sum/=(i+1)
    print(int(sum))
