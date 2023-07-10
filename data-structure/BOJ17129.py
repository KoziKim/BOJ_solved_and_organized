import sys
put = sys.stdin.readline

n, m = map(int, input().split())

hash = {}

for i in range(n):
    x = put().rstrip()
    addr, pswd = x.split()
    hash[addr] = pswd

for i in range(m):
    addr = put().rstrip()
    print(hash[addr])