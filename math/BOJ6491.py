while True:
    nums = list(map(int, input().split()))
    for i in range(len(nums)):
        a = nums[i]
        if a == 0:
            break
        if a == 1:
            print("1 DEFICIENT")
            continue
        sum = 0
        for j in range(1, a//2+1):
            if a%j == 0:
                sum += j
        if sum > a:
            print(a, "ABUNDANT")
        elif sum < a:
            print(a, "DEFICIENT")
        elif sum == a:
            print(a, "PERFECT")
    if a == 0:
        break