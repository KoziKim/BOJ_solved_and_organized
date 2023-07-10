n, m = map(int, input().split())

a = list(map(int, input().split()))
a.sort()
s = []

def dfs(start):
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    
    for i in range(start, n):
        s.append(a[i])
        dfs(i)
        s.pop()
dfs(0)