n = int(input())
with open("File3.txt", "r") as file:
    lines = file.readlines()
    
    for i in range(0, n):
        print(lines[i])
        if n > len(lines):
            break