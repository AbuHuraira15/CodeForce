a=int(input())
x,y,z=0,0,0
for i in range(a):
    d,e,f=map(int,input().split())
    x+=d
    y+=e
    z+=f
if x==0 and y==0 and z==0:
    print("YES")
else:
    print("NO")