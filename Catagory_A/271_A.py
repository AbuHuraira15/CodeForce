n=int(input())
while True:
    n+=1
    a=n//1000
    b=n//100%10
    c=n//10%10
    d=n%10
    if len({a,b,c,d})==4:
        break
print(n)