a, b = map(int, input().split())

def facto(x):
    if x == 0 or x == 1:
        return 1
    return x*facto(x-1)

print(int(facto(a)/(facto(a-b)*facto(b))))