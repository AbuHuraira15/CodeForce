n = int(input())
b = {}
for i in range(n):
    a = input()
    if a in b:
        b[a] += 1
    else:
        b[a] = 1

print(max(b, key=b.get))
