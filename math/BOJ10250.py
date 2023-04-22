from math import ceil
t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    if ceil(n / h) < 10:
        if n % h == 0:
            print(h, 0, ceil(n / h), sep ='')
        else:
            print(n % h, 0, ceil(n / h), sep ='')
    else:
        if n % h == 0:
            print(h, ceil(n / h), sep ='')
        else:
            print(n % h, ceil(n / h), sep ='')