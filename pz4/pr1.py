file = str(input("Введите имя файла: "))
open(f"{file}", "x")
print("Начните вводить строки")
while True:
    a = str(input())
    if a == "":
        break
    with open(f"{file}", "w") as f:
        f.write(a + "\n")
