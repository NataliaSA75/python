a = int(input("Введите число от 0 до 256 "))

if a >= 256:
    print("Число не подходит")
else:
    result = []
    while a:
        result.append(a % 2)
        a //= 2
    result.reverse()
    print(result)