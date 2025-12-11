n,L=map(int,input().split())
a=sorted(map(int,input().split()))
max_gap=max(a[0],L-a[-1])
for i in range(n - 1):
    max_gap=max(max_gap,(a[i+1]-a[i])/2)
print(max_gap)
