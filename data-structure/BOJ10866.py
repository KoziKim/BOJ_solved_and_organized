import sys
from collections import deque
n = int(input())

q = deque()
for i in range(n):
    inst = sys.stdin.readline().split()
    if inst[0] == "push_back":
        q.append(inst[1])
    elif inst[0] == "push_front":
        q.appendleft(inst[1])
    elif inst[0] == "front":
        try:
            print(q[0])
        except:
            print(-1)
    elif inst[0] == "back":
        try:
            print(q[-1])
        except:
            print(-1)
    elif inst[0] == "size":
        print(len(q))
    elif inst[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif inst[0] == "pop_front":
        try:
            print(q.popleft())
        except:
            print(-1)
    elif inst[0] == "pop_back":
        try:
            print(q.pop())
        except:
            print(-1)