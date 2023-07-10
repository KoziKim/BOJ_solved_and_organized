n = int(input())

def fact(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    return x*fact(x-1)

a = fact(n)
b = list(str(a))
cnt = 0
while b[-1] == "0":
    if b[-1] == "0":
        cnt += 1
        b.pop()
print(cnt)