a = input()
x = 0
for ch in a:
    if ch == '4' or ch == '7':
        x += 1

if x == 4 or x == 7:
    print("YES")
else:
    print("NO")
