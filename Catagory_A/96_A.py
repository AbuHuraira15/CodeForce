a=input()
x,y=0,0
for ch in a:
    if ch =="1":
        x+=1
        y=0
    else:
        y+=1
        x=0
    if x==7 or y==7:
        break
if x==7 or y==7:
    print("YES")
else:
    print("NO")
