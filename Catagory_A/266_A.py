a=int(input())
b=input()
x,y=0,0
for i in range (len(b)-1):
    if b[i]==b[i+1]:
        x=x+1
print(x)