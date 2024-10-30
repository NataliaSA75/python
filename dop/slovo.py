

while True:
    word = str(input("Enter word "))
    wordArray = list(word)
    if  (len(wordArray) > 3) & word.isalpha():
        print(word)
        break
file_name = input("File name is ")
with open(f"{file_name}.txt", "x") as file:
    file.write(word)