output = open('deb.txt', 'w')
units = int(input('Enter No of Units'))

if units <= 64:
    light_bill = 64 * 5
    output.write("Bill for this month is " + str(light_bill))
else:
    light_bill = 64 * 5
    over = units - 64
    new_bill = light_bill + (over * 10)
    output.write("Bill for this month is " + str(new_bill))
