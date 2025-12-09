a=input()
b=[]
for i in range(0,len(a)):
    if a[i]!="+":
        b.append(a[i])
b.sort()
for i in range(0,len(b)):
    if i<len(b)-1:
        print(f"{b[i]}+",end="")
    else:
        print(b[i])