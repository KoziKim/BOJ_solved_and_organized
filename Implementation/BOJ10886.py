n = int(input())
cute = 0
not_cute = 0
for i in range(n):
    a = int(input())
    if a == 1:
        cute += 1
    elif a == 0:
        not_cute += 1
if cute > not_cute:
    print("Junhee is cute!")
elif cute < not_cute:
    print("Junhee is not cute!")