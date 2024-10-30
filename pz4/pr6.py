n = int(input())
with open("File3.txt", "r") as file:
    lines = file.readlines()
    if n <= len(lines):
        for i in range(len(lines)-1,len(lines)-n-1, -1):
            print(lines[i])