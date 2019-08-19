list = []
for i in range(3500,5001):
    if i%7 == 0 and i%9 != 0:
        list.append(i)
        
print(list)
