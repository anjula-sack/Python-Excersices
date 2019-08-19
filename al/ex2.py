no = int(input("Enter Last Number"))
dicts = []
for i in range(1, no + 1):
    a = i * i
    dict = {i: a}
    dicts.append(dict)
print(dicts)

for i in range(0,len(dicts)):
    print(dicts[i])
