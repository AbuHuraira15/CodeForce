import math
a,b=map(int,input().split())
c=math.ceil(a/2)
if b<=c:
    print(b*2-1)
else:
    b=b-c
    print(b*2)
