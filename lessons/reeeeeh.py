# import builtins
# # встроенные функции
import pprint
# name = {'kate': 1, 'Masha': 2}
# sirname = {'ivanova': 1, 'YYY': 2} 
# ss = [name, sirname]
# pprint.pprint(ss)
# # пакеты, в них можно объединять модули
a = ['a', 'd', 'w']
# b = list(enumerate(a, 56))
# print(b)
# print(list(zip(a, b)))
def prefix(s, prefix = "prefix_"):
    return prefix + s

def long_enough(s):
    return s == 'a'or s == 'w'

print(list(map(prefix, a)))
print(list(filter(long_enough, a)))

pprint.pprint(locals())
pprint.pprint(globals())
# определение глобальной области видимости
v1 = "global v1"
