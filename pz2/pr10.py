# 8 для всех
def IsEndFour(i):
    l = list(str(i))
    lenght = len(l)
    return int(l[lenght-1])

def IsEndEight(i):
    l = list(str(i))
    length = len(l)
    return int(l[length-1])

for i in  range(10, 100):
    if IsEndFour(i*3) == 4:
        print(i)
    if IsEndEight(i*2) == 8:
        print(i)