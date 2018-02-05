a = int(input())
b = int(input())
c = int(input())

r = str(a * b * c)

for i in '0123456789':
    print(len(r.split(i)) - 1)
