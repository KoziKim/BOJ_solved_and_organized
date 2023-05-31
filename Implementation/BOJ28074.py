a = input()

cnt_m = 0
cnt_o = 0
cnt_b = 0
cnt_i = 0
cnt_s = 0
for i in range(len(a)):
    if a[i] == "M":
        cnt_m += 1
    if a[i] == "O":
        cnt_o += 1
    if a[i] == "B":
        cnt_b += 1
    if a[i] == "I":
        cnt_i += 1
    if a[i] == "S":
        cnt_s += 1
if cnt_m >= 1 and cnt_o >= 1 and cnt_b >= 1 and cnt_i >= 1 and cnt_s >= 1:
    print("YES")
else:
    print("NO")