n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(len(nums)):
        if nums[i] not in s:
            s.append(nums[i])
            dfs()
            s.pop()

dfs()