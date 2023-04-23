while True:
    lines = list(map(int, input().split()))
    if sum(lines) == 0:
        break
    lines.sort()
    if lines[2] ** 2 == lines[0] ** 2 + lines[1] ** 2:
        print('right')
    else:
        print('wrong')