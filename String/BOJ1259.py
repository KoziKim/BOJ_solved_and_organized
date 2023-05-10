import sys
while True:
    a = list(sys.stdin.readline().rstrip())
    if a[0] == '0':
        break
    b = []
    for i in range(len(a)):
        b.append(a[len(a)-1-i])
    if a == b:
        print('yes')
    else:
        print('no')