# по вариантам 3, здесь шестой номер
import datetime

start = datetime.timedelta(hours = int(input("Start hour: ")), minutes = int(input("Start minute: ")))
l_duration = datetime.timedelta(hours = int(input()), minutes = int(input()))

print("Break duration:")
b_duration = datetime.timedelta(hours = int(input("Start hour: ")), minutes = int(input("Start minute: ")))
breakAfter = [int(x) for x in input("After lessons with number: ").split()]

print("Big break duration:")
bb_duration = datetime.timedelta(hours = int(input("Start hour: ")), minutes = int(input("Start minute: ")))
bigBreakAfter = [int(x) for x in input("After lessons with number: ").split()]

n = int(input("Number of lessons: "))

for i in range(1, n+1):
    if i == 1:
        print("Lesson")
        print(f"{start}")
    else:
        print("Lesson")
        print(f"{start + l_duration}")
        start += l_duration
    if i in list(breakAfter):
        print("Break")
        print(f"{start + b_duration}")
        start+=b_duration  
    if i in list(bigBreakAfter):
        print("Big break")
        print(f"{start + bb_duration}")
        start+=bb_duration 


