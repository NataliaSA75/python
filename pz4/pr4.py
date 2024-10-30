
files = []
while True:
   file = str(input())
   if file == "":
      break
   files.append(file) 

with open("output4.txt", "w") as output_file:
   for file in files:
      with open(file, "r") as input_file:
         strings = input_file.read()
         output_file.write(strings)
         
