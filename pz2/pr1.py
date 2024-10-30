day1 = float(input())
numberOfDays =int(input())
# переделано под рассчет всего расстояния за заданное количество дней
sum = 0
i = 1
while i <= numberOfDays:
    if i == 1:
        sum += day1
        print(day1)
    else:
        k = day1*10/100
        day1 += k
        print(day1)
        sum += day1
    i+=1
print(sum)