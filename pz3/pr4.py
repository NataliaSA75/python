a = [1,2,3,4,10,20]   

if 20 in a:
    num = 20
    index = a.index(num)
    a.insert(index, 200)

a.pop()
print(a)