x = []
y = []

for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()
x_set = list(set(x))
y_set = list(set(y))
small_x = 0
big_x = 0
small_y = 0
big_y = 0

for i in range(3):
    if x[i] == x_set[0]:
        small_x += 1
    elif x[i] == x_set[1]:
        big_x += 1
    if y[i] == y_set[0]:
        small_y += 1
    elif y[i] == y_set[1]:
        big_y += 1

if small_x > big_x:
    nx = x_set[1]
elif small_x < big_x:
    nx = x_set[0]
if small_y > big_y:
    ny = y_set[1]
elif small_y < big_y:
    ny = y_set[0]

print(nx, ny)