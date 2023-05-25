from decimal import Decimal
a, b, c = map(int, input().split())
A = Decimal(a*b)
print(Decimal(A/c))