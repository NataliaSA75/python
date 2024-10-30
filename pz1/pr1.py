hight = int(input())
weight = int(input())
optimal_weight = hight - 100
if optimal_weight < weight:
    print("Вам нужно сбросить вес")
elif optimal_weight > weight:
    print("Вам нужно набрать вес")
else:
    print("У Вас идеальный вес")