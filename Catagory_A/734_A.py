n= int(input())
b=input()
x,y=0,0
for ch in b:
    if ch=="A":
        x+=1
    else:
        y+=1
if x>y:
    print("Anton")
elif x<y:
    print("Danik")
else:
    print("Friendship")