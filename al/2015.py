output = open('mark.txt', 'a')
index = int(input("Enter The Index"))

while index != -1:
    output.write("Index_no" + str(index))
    a = 0
    while a != 3:
        output.write(",")
        mark = int(input("Enter Marks"))
        output.write(str(mark))
        a += 1
    output.write("\n")
    index = int(input("Enter The Index"))

output.close()
