print("start")
try:
    val =  int(input())
    tmp = 10/val
    print(tmp)
except(ValueError, ZeroDivisionError):
    print("Error")
finally:
    print("end")