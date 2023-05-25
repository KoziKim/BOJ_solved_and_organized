import sys
n = int(input())

member = []
for i in range(n):
    member.append(sys.stdin.readline().split())

member.sort(key = lambda x:int(x[0]))

for mem in member:
    print(*mem)