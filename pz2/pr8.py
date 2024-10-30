# шестое для всех
n = int(input())

def getNumberOfDiv(i):
    num = 0
    for j in range(1, i+1):
        if i%j == 0:
            num+=1
    return num
#print(f"{getNumberOfDiv(12)}")

for i in range(1, 201):
    if n == getNumberOfDiv(i):
        print(i)