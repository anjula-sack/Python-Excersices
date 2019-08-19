items = [10, 12, 15, 10, 25, 45, 50, 25, 10, 12]

item_no = int(input("Enter Item No"))
total = 0
while item_no != -1:
    q = int(input("Enter Quantity of the item"))
    no = item_no - 1
    net = items[no] * q
    total = total + net
    item_no = int(input("Enter Item No"))
print("Total Price Is ", total)
