x, y = map(int, input().split())
arr = list(map(int, input().split()))

count1 = 0
k_score = arr[y - 1]   

for i in range(x):
    if arr[i] >= k_score and arr[i] != 0:
        count1 += 1

print(count1)
