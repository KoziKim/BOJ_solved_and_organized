# 도착까지 n미터 남음, t분 남음

# 스쿠터 x m/s로 움직임

# 공원 안은 속도제한걸려서 y m/s로 움직이고 공원 입구까지의 거리가 m미터

# 제때 도착한다면 0을, 아니라면 걸리는 시간을 분단위로 올림하여 출력

from math import ceil

n, t = map(int, input().split())
m = int(input())
x, y = map(int, input().split())

if t >= m / (x*60) + (n - m) / (y*60):
    print(0)
else:
    print(ceil((m / (x*60) + (n - m) / (y*60)))-t)