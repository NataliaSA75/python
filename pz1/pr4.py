year = int(input())

if (year%4 == 0 and year%100 != 0) or (year%4 == 0 and year%100 == 0 and year%400 == 0):
    print("Високосный год")
else:
    print("Невисокосный год")