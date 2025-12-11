a=input()
x,y=0,0
for i in range(len(a)):
    if 'A' <= a[i] <= 'Z':
        x+=1
    elif 'a' <= a[i] <= 'z':
        y+=1
if x<=y:
    print(a.lower())
else:
    print(a.upper())