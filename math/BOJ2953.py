first = 0
who = 1
for i in range(5):
    a = list(map(int, input().split()))
    if sum(a) > first:
        first = sum(a)
        who = i+1

print(who, first)