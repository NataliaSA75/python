a = [1, 2, 3, 4, 5]               
b = [4, 5, 6, 7, 8]
c = []
for item in b:
    if item not in a:
        c.append(item)

print(c)