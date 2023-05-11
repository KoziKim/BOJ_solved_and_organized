b = int(input())

Ot = b
if b >= 300:
    Vic = b - 300
else:
    Vic = 2100 + b
if b >= 200:
    Edm = b - 200
else:
    Edm = 2200 + b
if b >= 100:
    Winn = b - 100
else:
    Winn = 2300 + b
Tor = b
if b < 2300:
    Hali = b + 100
else:
    Hali = b - 2300

St = b + 130

if St < 0:
    St = St + 2360
if St % 100 >= 60:
    St = St + 40
if St >= 2400:
    St = St - 2400

print(f"""{Ot} in Ottawa
{Vic} in Victoria
{Edm} in Edmonton
{Winn} in Winnipeg
{Tor} in Toronto
{Hali} in Halifax
{St} in St. John's""")