import math
x = float(input())
y = float(input())
if y > 0:
    if math.sqrt(y) >= x and x >= -1 and 0 <= y <= 1:
        print("Число принадлежит закрашенной области")
else:
    print("Число не принадлежит закрашенной области")
    