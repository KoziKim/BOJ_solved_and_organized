n = int(input())

for i in range(n):
    print((n-1-i)*" ", "*", sep = '', end = '')
    if i >= 1:
        for j in range(i):
            print(" *", end = '')
    print()