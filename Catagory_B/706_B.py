import bisect

n=int(input())
path=list(map(int,input().split()))
x=int(input())
path.sort()
for i in range(x):
    a=int(input())
    d=bisect.bisect_right(path,a)
    print(d)