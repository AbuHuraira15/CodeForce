a,b=map(int,input().split())
while b>0:
    if a%10!=0:
        a-=1
        b-=1
    else:
        a=a//10
        b-=1
if a>=0:
    print(a)
else:
    print(0)