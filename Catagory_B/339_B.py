a,b=map(int,input().split())
path=map(int,input().split())
last=1
total=0
for x in path:
    if last<=x:
        total+=(x-last)
        last=x
    else:
        d=a-last+1
        total=total+d+(x-1)
        last=x
print(total)