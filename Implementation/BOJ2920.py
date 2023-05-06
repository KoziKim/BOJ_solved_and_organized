melody = list(map(int, input().split()))

if melody == sorted(melody):
    print("ascending")
elif melody == sorted(melody, reverse=True):
    print("descending")
else:
    print("mixed")