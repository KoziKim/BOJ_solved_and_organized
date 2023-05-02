import sys

h, m, s = map(int, input().split())

now = 3600*h + 60*m + s

q = int(input())
for i in range(q):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
        now += query[1]
        now %= 86400
    if query[0] == 2:
        now -= query[1]
        now %= 86400
    if query[0] == 3:
        print(now//3600, (now%3600)//60, now%60)