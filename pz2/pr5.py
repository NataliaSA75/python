n = int(input())
if n < 0:
    print("oshibka")
else:
    sum = 0
    for i in range(1, n+1, 2):
        if n%i == 0:
            sum+=i
            print(i)
    print(sum)