while True:
    try:
        s, n = map(int, input().split())
    except:
        break
    dragons = []
    for _ in range(n):
        x, y = map(int, input().split())
        dragons.append((x, y))
    dragons.sort()
    ok = True
    for x, y in dragons:
        if s <= x:
            ok = False
            break
        s += y
    if ok:
        print("YES")
    else:
        print("NO")
