t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    if a == 1:
        A = 5000000
    elif 2 <= a <= 3:
        A = 3000000
    elif 4 <= a <= 6:
        A = 2000000
    elif 7 <= a <= 10:
        A = 500000
    elif 11 <= a <= 15:
        A = 300000
    elif 16 <= a <= 21:
        A = 100000
    elif a == 0 or a >= 22:
        A = 0
    if b == 1:
        B = 5120000
    elif 2 <= b <= 3:
        B = 2560000
    elif 4 <= b <= 7:
        B = 1280000
    elif 8 <= b <= 15:
        B = 640000
    elif 16 <= b <= 31:
        B = 320000
    if b == 0 or b >= 32:
        B = 0
    print(A+B)
