import sys
put = sys.stdin.readline
n, m = map(int, input().split())

d = {}
for i in range(n):
    d[put().rstrip()] = 1

db = {}

for i in range(m):
    try:
        a = put().rstrip()
        if d[a]:
            db[a] = 1
    except:
        continue
print(len(db))
c = []
for _ in db:
    c.append(_)
c.sort()
for _ in c:
    print(_)