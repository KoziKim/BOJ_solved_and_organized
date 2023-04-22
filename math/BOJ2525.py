h, m = map(int, input().split())
time = int(input())

res = h*60 + m + time
if (res // 60) >= 24:
    print(res // 60 - 24, res % 60)
else:
    print(res // 60, res % 60)