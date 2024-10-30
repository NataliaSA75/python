filename = input("Введите имя файла: ")
n = int(input("Введите максимальное количество строк: "))

with open(filename, 'r') as file:
    lines = file.readlines()

file_count = 1
for i in range(0, len(lines), n):
    with open(f"{file_count}.txt", 'w') as output_file:
        output_file.writelines(lines[i:i+n])
    file_count += 1

print(f"Создано {file_count - 1} файлов.")