a = 0
b = 0
c = 0

n = int(input())

while True:
    if n >= 300:
        n -= 300
        a += 1
    elif n >= 60:
        n -= 60
        b += 1
    elif n >= 10:
        n -= 10
        c += 1
    elif n < 10:
        print(-1)
        break
    if n == 0:
        print(a, b, c)
        break
