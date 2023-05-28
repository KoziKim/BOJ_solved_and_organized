a, b, c = map(int, input().split())

if b == a + c-a:
    print("Anything")
elif b < a + c-a:
    print("Bus")
else:
    print("Subway")