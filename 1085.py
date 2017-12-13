x, y, w, h = map(int, raw_input().split(" "))
a = w - x
b = h - y
print(min(a, b, x, y))