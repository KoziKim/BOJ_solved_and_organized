n, m = map(int, input().split())

a = list(map(int, input().split()))
a.sort()
s = []
visited = [False] * n
ans = []
def dfs():
    prev = 0
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(len(a)):
        if a[i] != prev and visited[i] == False:
            s.append(a[i])
            prev = a[i]
            visited[i] = True
            dfs()
            s.pop()
            visited[i] = False

dfs()
