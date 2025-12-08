a,b,c=map(int,input().split())
x=0
y=0
if a%c==0:
    x=a/c
else:
    x=(a//c)+1
if b%c==0:
    y=b/c
else:
    y=(b//c)+1
print(int(x*y))