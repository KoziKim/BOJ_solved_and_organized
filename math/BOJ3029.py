a = list(map(int, input().split(":")))
b = list(map(int, input().split(":")))

now = a[0]*3600 + a[1]*60 + a[2]
throw = b[0]*3600 + b[1]*60 + b[2]

if throw > now:
    wait = throw - now
else:
    wait = 24*3600 + throw - now

h = (wait - wait%3600)//3600
m = (wait - h*3600)//60
s = wait%60 

if h < 10:
    h = "0" + str(h)
if m < 10:
    m = "0" + str(m)
if s < 10:
    s = "0" + str(s)

print(f"{h}:{m}:{s}")