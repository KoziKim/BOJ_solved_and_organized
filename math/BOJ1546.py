n = int(input())

scores = list(map(int, input().split()))

m = max(scores)
fixed = []
for score in scores:
    fixed.append(score/m*100)

print(sum(fixed)/n)