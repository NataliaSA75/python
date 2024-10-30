r1 = float(input())
r2 = float(input())
string = int(input("Сопротивление: последовательное - 1, параллельное - 2"))

if string == 1:
    print(r1+r2)
else:
    print(1/r1 + 1/r2)