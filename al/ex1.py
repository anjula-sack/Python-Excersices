list = [0, 3, 64, 6, 32, 43, 73, 98, 45, 34, 76, 37, 39]
a = int(input("Enter no"))
result = list[0]

for i in range(0, len(list)):
    if list[i] == a:
        result = list[i]
        break
print(result)

