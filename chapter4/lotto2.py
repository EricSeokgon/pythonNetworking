import random

pick = set()
while len(pick) < 6:
    n = random.randint(1, 45)
    if n not in pick:
        pick.add(n)

print(pick)
print(sorted(pick))
