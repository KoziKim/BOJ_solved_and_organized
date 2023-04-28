from itertools import permutations
nums = list(map(int, input().split()))
comb_ = list(permutations(nums, 3))

candi = []
for com in comb_:
    candi.append(max(com[0]*com[1]+com[2], com[0]*com[1]-com[2],
                     com[0]+com[1]*com[2], com[0]+com[1]-com[2], 
                     com[0]-com[1]*com[2], com[0]-com[1]+com[2]))
print(max(candi))