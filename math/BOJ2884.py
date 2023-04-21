h, m = map(int, input().split())

res = h*24*60 + (m-45)

if (res // (24*60)) < 0:
    print(res // (24*60) +24, res % 60)
else:
    print(res // (24*60), res % 60)