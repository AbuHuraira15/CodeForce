n=int(input())
d=0
for i in range(1,n+1):
    a,b,c=map(int,input().split())
    if a==b==1 or b==c==1 or c==a==1:
        d=d+1
print(d)