# 7 для всех
def innerSum(l):
    return int(l[1])+int(l[2])
def outterSum(l):
    return int(l[0])+int(l[3])
for i in range(1000, 10000):
    l = list(str(i))
    if innerSum(l) == outterSum(l):
        print(i)