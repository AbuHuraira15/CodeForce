a,b,c=map(int,input().split())
total=0
for i in range(1,c+1,1):
    t=a*i
    total+=t
if total>b:
    print(total-b)
else:
    print(0)