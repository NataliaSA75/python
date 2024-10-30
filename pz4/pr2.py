file = str(input("Введите имя файла: "))
with open(f"{file}") as f:
    #s = sum(1 for _ in f)
    i = 1
    for line in f:
        print(f"{i}  " + line.rstrip())
        i += 1
