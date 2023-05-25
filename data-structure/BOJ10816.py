n = int(input())
nums = list(map(int, input().split()))
m = int(input())
check_nums = list(map(int, input().split()))

dict = {}

for i in nums:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

for i in check_nums:
    if i in dict:
        print(dict[i], end = ' ')
    else:
        print(0, end = ' ')