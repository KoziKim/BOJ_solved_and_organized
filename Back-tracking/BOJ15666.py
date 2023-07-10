n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

s = []

def dfs(start):
    prev = 0
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n):
        if nums[i] != prev:
            s.append(nums[i])
            prev = nums[i]
            dfs(i)
            s.pop()

dfs(0)