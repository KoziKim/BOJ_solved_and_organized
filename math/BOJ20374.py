import sys
ans = 0
while True:
    try:
        a = float(sys.stdin.readline().strip())
        ans += a*100
    except:
        ans /= 100
        print("%.2f"%ans)
        break