# шестое задание по вариантам
c = []
less =[]
med = []
more = []

while True:
    a = input("Введите число: ")
    if a == "":
        break
    c.append(int(a))

print(c)

sum = sum(c)
print(sum)
print(len(c))
sr_ar = sum / len(c)
print(sr_ar)

sorted_c = sorted(c)
for i in range(len(sorted_c)):
    if sorted_c[i] < sr_ar:
        less.append(c[i])
    if sorted_c[i] == sr_ar:
        med.append(c[i])
    if sorted_c[i] >sr_ar:
        more.append(c[i])

print("Числа меньше среднего:")
print(less)
print("Числа равные среднему:")
print(med)
print("Числа больше среднего:")
print(more)