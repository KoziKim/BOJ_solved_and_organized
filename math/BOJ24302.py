a, b = map(int, input().split())

def company_one(dist):
    if dist <= 5:
        return 4
    elif 5 < dist <= 10:
        return 7
    elif 10 < dist <= 20:
        return 12
    elif 20 < dist <= 30:
        return 17
    elif 30 < dist:
        return dist*0.57
    
def company_two(dist):
    if dist <= 2:
        return 0.9 + 0.9*dist
    elif 2 < dist <= 5:
        return 1 + 0.85*dist
    elif 5 < dist <= 20:
        return 1.25 + 0.8*dist
    elif 20 < dist <= 40:
        return 3.25 + 0.7*dist
    elif 40 < dist:
        return 9.25 + dist*0.55
a = a//1000
b = b//1000
p1 = min(company_one(a), company_two(a))
p2 = min(company_one(b), company_two(b))

print("%.2f"%(p1 + p2))