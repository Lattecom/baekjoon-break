# 13199

T = int(input())

for _ in range(T):
    P, M, F, C = map(int, input().split(" "))

    cnt = 0
    coupon = ((M // P) * C)
    x = coupon // F
    while(coupon >= F):
        cnt += coupon // F
        coupon = (coupon // F)*C + coupon % F

    print((cnt-x))