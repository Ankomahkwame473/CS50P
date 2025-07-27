from collections import Counter
item = []
while True:
    try:
        grocery = input("").upper()
    except EOFError:
        break
    else:
        item.append(grocery)
        item.sort()
a = dict(Counter(item))
groc = list(a.keys())
num = list(a.values())
for i in range(len(a)):
    print(f"{num[i]} {groc[i]}")
