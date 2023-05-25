word = input()

chrs = [0 for _ in range(26)]

for i in range(len(word)):
    if 97 <= ord(word[i]) <= 122:
        chrs[ord(word[i])-97] += 1
    elif 65 <= ord(word[i]) <= 90:
        chrs[ord(word[i])-65] += 1

max_num = max(chrs)
cnt = 0
for i in range(len(chrs)):
    if chrs[i] == max_num:
        cnt += 1

if cnt > 1:
    print("?")
else:
    print(chr(chrs.index(max(chrs))+65))