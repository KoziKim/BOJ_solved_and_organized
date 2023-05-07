remain = set()

for i in range(10):
    remain.add(int(input())%42)

print(len(remain))