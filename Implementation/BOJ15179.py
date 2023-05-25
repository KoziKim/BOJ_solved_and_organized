a = input()
b = input()
a_score = 0
b_score = 0
n = int(input())
events = list(input())
for i in range(n):
    if i%2 == 0:
        if events[i] == "S":
            continue
        elif events[i] == "H":
            a_score += 1
        elif events[i] == "D":
            if a_score == 6:
                a_score += 1
                break
            a_score += 2
        elif events[i] == "O":
            b_score += 1
    elif i%2 == 1:
        if events[i] == "S":
            continue
        elif events[i] == "H":
            b_score += 1
        elif events[i] == "D":
            if b_score == 6:
                b_score += 1
                break
            b_score += 2
        elif events[i] == "O":
            a_score += 1
    if a_score >= 7 or b_score >=7:
        break

if a_score < 7 and b_score < 7:
    if a_score > b_score:
        print(f"{a} {a_score} {b} {b_score}. {a} is winning.")
    elif a_score < b_score:
        print(f"{a} {a_score} {b} {b_score}. {b} is winning.")
    elif a_score == b_score:
        print(f"{a} {a_score} {b} {b_score}. All square.")
else:
    if a_score > b_score:
        print(f"{a} {a_score} {b} {b_score}. {a} has won.")
    elif a_score < b_score:
        print(f"{a} {a_score} {b} {b_score}. {b} has won.")
    elif a_score == b_score:
        print(f"{a} {a_score} {b} {b_score}. All square.")