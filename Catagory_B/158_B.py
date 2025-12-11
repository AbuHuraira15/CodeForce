li = [0, 0, 0, 0, 0]
n = int(input())
b = []
while len(b) < n:
    parts = input().strip().split()
    for p in parts:
        if p:
            b.append(int(p))
            if len(b) == n:
                break

for i in range(n):
    li[b[i]] += 1
tax = li[4]
tax += li[3]
li[1] = max(0, li[1] - li[3])
tax += li[2] // 2
if li[2] % 2 == 1:
    tax += 1
    li[1] = max(0, li[1] - 2)
tax += (li[1] + 3) // 4
print(tax)
