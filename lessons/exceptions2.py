print("start")
try:
    val =  int(input())
    tmp = 10/val
    print(tmp)
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print("end")