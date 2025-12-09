name = input()
name = name.lower()

for letter in name:
    if letter not in "aeiouy":
        print("." + letter, end="")

print()
