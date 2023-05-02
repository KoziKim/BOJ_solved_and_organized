# a, b = map(int,input().split())
# q, r = a//b, a%b
# if a != 0 and r < 0:
#     q, r = q+1, r-b
# print(q)
# print(r)

a, b = map(int,input().split())
q, r = divmod(a, b)
if a != 0 and r < 0:
    q, r = q+1, r-b
print(q)
print(r)