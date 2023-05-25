import sys
n = int(input())
ans = []
for i in range(n):
    ans.append(list(map(int, sys.stdin.readline().split())))
ans.sort(key=lambda x:x[1])
ans.sort()
for a in ans:
    print(*a)