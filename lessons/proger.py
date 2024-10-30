pr = 11
prog = pr
pr = pr%100
pr= pr // 1
print(pr)
if 9 < pr <= 14:
    print(f"{prog} программистов")
else:
    pr = prog
    pr = pr%10
    pr = pr // 1
    if pr == 0 or pr == 5 or pr == 6 or pr == 7 or pr == 8 or pr == 9:
        print(f"{prog} программистов")
    elif pr == 1:
        print(f"{prog} программист")
    elif pr == 2 or pr == 3 or pr == 4:
        print(f"{prog} программиста")