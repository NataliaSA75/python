a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("Равносторонний треугольник")
elif a == b or b == c or a == c:
    print("Равнобедренный треугольник")
else:
    print("Разносторонний треугольник")