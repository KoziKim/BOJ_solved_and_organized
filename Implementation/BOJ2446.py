n = int(input())

for i in range(n-1):
    print(" "*i, "*"*(2*(n-1-i) + 1), sep = '')

for i in range(n):
    print(" "*(n-1-i), "*"*(2*i + 1), sep = '')