n = int(input())
i = 2
prim = []
while i * i <= n:
    while n % i == 0:
        prim.append(i)
        n = n / i
    i = i + 1
if n > 1:
    prim.append(n)
print(prim)