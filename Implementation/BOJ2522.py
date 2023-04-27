n = int(input())

for i in range(1, n):
    print((n-i)*" ", i*"*", sep = '')

for i in range(n):
    print((i)*" ", (n-i)*"*", sep = '')