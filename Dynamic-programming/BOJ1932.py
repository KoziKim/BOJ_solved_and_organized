import sys
put = sys.stdin.readline
n = int(input())

dp = [0 for _ in range(n)]
tri = []
for i in range(n):
    tri.append(list(map(int, put().split())))

if n == 1:
    print(tri[0][0])
    exit()

dp[0] = tri[0][0] + tri[1][0]
dp[1] = tri[0][0] + tri[1][1]

for i in range(2, n):
    for j in range(i-1, 0, -1):
        dp[j] = max(dp[j-1] + tri[i][j], dp[j] + tri[i][j])
    dp[0] += tri[i][0]
    dp[i] = 0
    for k in range(i+1):
        dp[i] += tri[k][k]

print(max(dp))


# dp[0] = tri[0][0]

# dp[0] = tri[0][0] + tri[1][0]
# dp[1] = tri[0][0] + tri[1][1]

# dp[1] = max(dp[0]+tri[2][1], dp[1]+tri[2][1])
# # dp[0] = tri[0][0] + tri[1][0] + tri[2][0]
# # dp[2] = tri[0][0] + tri[1][1] + tri[2][2]

# dp[1] = max(dp[0] + tri[3][1], dp[1] + tri[3][1])
# dp[2] = max(dp[1] + tri[3][2], dp[2] + tri[3][2])
# # dp[0] = tri[0][0] + tri[1][0] + tri[2][0] + tri[3][0]
# # dp[3] = tri[0][0] + tri[1][1] + tri[2][2] + tri[3][3]

# dp[1] = max(dp[0] + tri[4][1], dp[1] + tri[4][1])
# dp[2] = max(dp[1] + tri[4][2], dp[2] + tri[4][2])
# dp[3] = max(dp[2] + tri[4][3], dp[3] + tri[4][3])
# # dp[0] = tri[0][0] + tri[1][0] + tri[2][0] + tri[3][0] + tri[4][0]
# # dp[4] = tri[0][0] + tri[1][1] + tri[2][2] + tri[3][3] + tri[4][4]