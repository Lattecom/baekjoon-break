# 1149

from sys import stdin

class Test():
    s = ["3",
        "26 40 83",
        "49 60 57",
        "13 89 99"]
    c = -1

    def readline():
        Test.c += 1
        return Test.s[Test.c]

def main(inputInterface):

    N = int(inputInterface.readline())

    price = [0, 0, 0]

    for i in range(N):
        t = [0, 0, 0]
        r, g, b = map(int, inputInterface.readline().split())
        t[0] = r + min(price[1], price[2])
        t[1] = g + min(price[0], price[2])
        t[2] = b + min(price[0], price[1])
        price = t 

    print(min(price))

main(Test)