now = 0
tmp = [0 for _ in range(4)]

for i in range(4):
    a, b = map(int, input().split())
    if b > a:
        now = max(now, now-a+b)
    else:
        now = now - a + b
    tmp[i] = now

print(max(tmp))