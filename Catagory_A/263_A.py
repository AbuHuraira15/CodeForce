a=[]
for i in range(0,5,1):
    b=list(map(int,input().split()))
    a.append(b)
for i in range(5):
    for j in range(5):
        if a[i][j]==1:
            print(abs(i-2)+abs(j-2))
            break