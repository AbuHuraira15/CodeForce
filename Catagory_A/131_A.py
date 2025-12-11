s = input().strip()
ok = True
for c in s[1:]:
    if c.islower():
        ok = False
        break
if ok:
    if s[0].isupper():
        print(s.lower())
    else:
        print(s.capitalize())
else:
    print(s)
