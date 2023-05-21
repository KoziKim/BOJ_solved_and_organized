import sys
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == 0:
        break
    if (c-a)/b != (c-a)//b:
        print("X")
    else:
        if (c-a) < 0 and b >= 0:
            print("X")
        elif (c-a) > 0 and b <= 0:
            print("X")
        else:
            print((c-a)//b+1)
