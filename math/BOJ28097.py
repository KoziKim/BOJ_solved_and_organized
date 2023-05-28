n = int(input())
a = list(map(int, input().split()))
sum = 0
for i in range(n):
    if i == n-1:
        sum += a[i]
        break
    sum += a[i] + 8

print(sum//24, sum%24)