l = [1, 2, 3, 4, 5, 6, 7, 8]

for i, item in enumerate(l):
    if i in [2, 4, 6]:
        print(item)

# for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(item)