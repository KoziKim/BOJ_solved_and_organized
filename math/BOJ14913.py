a, b, c = map(int, input().split())

if (c-a)/b != (c-a)//b or (b > 0 and a > c) or (b < 0 and a < c):
    print('X')
else:
    print((c-a)//b + 1)