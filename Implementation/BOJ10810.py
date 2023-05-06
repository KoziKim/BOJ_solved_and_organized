n, m = map(int, input().split())

bowl = [0 for _ in range(n)]

for i in range(m):
    a, b, ball = map(int, input().split())
    for j in range(a-1, b):
        bowl[j] = ball

print(*bowl)