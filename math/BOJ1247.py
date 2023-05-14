import sys

for i in range(3):
    n = int(input())
    S = 0
    for j in range(n):
        S += int(sys.stdin.readline().rstrip())
    if S == 0:
        print("0")
    elif S > 0:
        print("+")
    elif S < 0:
        print("-")