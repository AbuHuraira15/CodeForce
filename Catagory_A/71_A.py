n=int(input())
for i in range(n):
    a=input()
    if len(a)>10:
        b=a[0]+str(len(a)-2)+a[len(a)-1]
        print(b)
    else:
        print(a)