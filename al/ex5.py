marks = int(input("Enter Marks"))
count = 0
while marks != -1:
    if marks < 40:
        count = count + 1
    marks = int(input("Enter Marks"))

print("No of Students: ",count)
