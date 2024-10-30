num = 620000
temp = 0.037
years = 1
while num <= 1500000:
    num = num + num*temp
    years+=1
print(years)