a=input()
word="hello"
x=0
j=0
for i in range(0,len(word)):
    while j<len(a):
        if word[i]==a[j]:
            x+=1
            j+=1
            break
        else:
            j+=1
if x==len(word):
    print("YES")
else:
    print("NO")