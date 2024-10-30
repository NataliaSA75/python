import random             
a = []
for i in range(10):
    num = random.randrange(1,100)
    a.append(num)
print(a)
print(a[1])
b = [j**2 for j in a]
print(b)