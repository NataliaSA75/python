import random
# gl = [x**2 for x in range(10)]
# print(gl)

# li = list(range(15))
# for i in range(10,16,2):
#     print(li[i])
#     break

# print("ihdeo")
# a: int = 5
# d: float = 12.12
# string: str = "sudh"
# print("sgdqw")
# try:
#     x = int(input("Input number: "))
#     if x == 0:
#         print(f"{x} = 0")
#     elif x > 0:
#         print(f"{x} > 0")
#     else:
#         print(f"{x} < 0")
# except(ValueError):
#     print("ValueError")

# phone = {'mur': 2321, 'mm': 3232}
# l = list(phone.keys())
# ll = list(phone.items())
# print(ll)

def g(y):
    y+=1
    print(y)

# g(56)
# print(id(g(86)))
# f = random.randint(12,45)
# list = ['papper', 'scissors', 'rock']
# f = random.randint(0, len(list)-1)
# print(list[f])

print(f"Первый игрок: {['papper', 'scissors', 'rock'][random.randint(0, 2)]}")
print(f"Второй игрок: {['papper', 'scissors', 'rock'][random.randint(0, 2)]}")


#
# print(f)