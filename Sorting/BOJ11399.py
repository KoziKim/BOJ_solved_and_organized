n = int(input())

p = list(map(int, input().split()))

p.sort()
sum = 0
for i in range(n):
    tmp = 0
    for j in range(i+1):
        tmp += p[j]
    sum += tmp
print(sum)