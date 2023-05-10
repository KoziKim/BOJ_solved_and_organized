import sys
inp = sys.stdin.readline
i = 1
while True:
    a, b, c = map(int, inp().split())
    if a == b == c == 0:
        break
    print(f'Triangle #{i}')
    if a == -1:
        if b < c:
            a = (c**2 - b**2)**(1/2)
            print("a =", "%0.3f"%a)
        else:
            print('Impossible.')
    elif b == -1:
        if a < c:
            b = (c**2 - a**2)**(1/2)
            print("b =", "%0.3f"%b)
        else:
            print('Impossible.')
    elif c == -1:
        c = (a**2 + b**2)**(1/2)
        print("c =", "%0.3f"%c)
    i += 1
    print()