# itertools 활용 풀이

# from itertools import combinations

# n, m = map(int, input().split())

# if m == 1:
#     for i in range(n):
#         print(i+1)
# else:
#     a = [i for i in range(1, n+1)]
#     b = list(combinations(a, m))
#     b.sort()
#     for i in b:
#         print(*i)

n, m = map(int, input().split())

s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()

dfs(1)