import math

n = int(input())
b = []

while len(b) < n:
    parts = input().split()
    for p in parts:
        b.append(int(p))
        if len(b) == n:
            break

def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

for a in b:
    root = int(math.isqrt(a))
    if root * root == a and is_prime(root):
        print("YES")
    else:
        print("NO")
