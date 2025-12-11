a,b=map(int,input().split())
path=map(int,input().split())
d=0
for x in path:
    if x<=b:
        d+=1
    else:
        d+=2
print(d)