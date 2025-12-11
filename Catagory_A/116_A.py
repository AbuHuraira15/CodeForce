n=int(input())
x,m=0,0
for i in range(n):
    a,b=map(int,input().split())
    x-=a
    x+=b
    m=max(m,x)
print(m)