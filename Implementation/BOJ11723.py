import sys

put = sys.stdin.readline
n = int(input())
S = set()

for i in range(n):
    x = put().split()
    if x[0] == "add":
        S.add(x[1])
        continue
    if x[0] == "check":
        if x[1] in S:
            print(1)
        else:
            print(0)
        continue
    if x[0] == "remove":
        if x[1] in S:
            S.remove(x[1])
        else:
            continue
        continue
    if x[0] == "toggle":
        if x[1] in S:
            S.remove(x[1])
        else:
            S.add(x[1])
        continue
    if x[0] == "all":
        S = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"}
        continue
    if x[0] == "empty":
        S = set()