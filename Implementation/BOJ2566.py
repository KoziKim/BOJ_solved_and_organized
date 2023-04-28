amax = 0
r = 1
c = 1
for i in range(1, 10):
    a = list(map(int, input().split()))
    for j in range(1, 10):
        if a[j-1] > amax:
            amax = a[j-1]
            r = i
            c = j
print(amax)
print(r, c)
