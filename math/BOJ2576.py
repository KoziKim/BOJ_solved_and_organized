ans = 0
odd = []
for i in range(7):
    a = int(input())
    if a % 2 != 0:
        ans += a
        odd.append(a)
if not odd:
    print(-1)
else:
    print(ans)
    print(min(odd))