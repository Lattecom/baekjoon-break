def fib(n):
    def go(count, prev, acc):
        if count == 0: 
            return 0
        elif count == 1:
            return acc
        else:
            return go(count-1, acc, prev+acc)
    return go(n,0,1)

a = int(input())

print(fib(a))