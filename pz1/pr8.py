x11 = int(input())
y11 = int(input())
x21 = int(input())
y21 = int(input())

x12 = int(input())
y12 = int(input())
x22 = int(input())
y22 = int(input()) # параллельность через проверку знаменателя, если он не равен нулю, то проверяем на параллельность

if x11 == x12 and y11 == y12 and x21 == x22 and y21 == y22:
    print("Отрезки лежат на одной прямой")
if (y21-y11)!=0 and (y22-y12)!=0:
    if ((x21-x11)/(y21-y11)) == ((x22-x12/(y22-y12))):
        print("Отрезки параллельны")
    else:
        a = x21 - x11
        b = y21 - y11
        c = x22 - x12
        d = y22 - y12
        if (c == 0 and x21>=x11 and x12<=x21 and (y12<=y11 or y12<=y21)):
            print("Пересекаются")
        else:
            print("Не пересекаются")
else:
    print("Ошибка вычислений")
