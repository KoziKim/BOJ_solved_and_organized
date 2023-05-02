p, k = map(int, input().split())

a = k
b = k
if p % 2 == 0:
    if 2 < k:
        print("BAD", 2)
    else:
        print("GOOD")
else:
    for i in range(3, k, 2):
        if p % i == 0:
            a = i
            b = p // i
            print("BAD", i)
            break
    else:
        print("GOOD")