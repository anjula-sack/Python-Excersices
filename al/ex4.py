temp = input("Enter Temperature")
tempo = []
for i in temp:
    tempo.append(i)
if tempo[-1] == "f" or tempo[-1] == "F":
    tempo.pop(-1)


    def convert(list):
        s = [str(i) for i in list]
        res = int("".join(s))
        return (res)


    x = convert(tempo)
    c = (x - 32) * 5 / 9
    print(c,"C")
elif tempo[-1] == "c" or tempo[-1] == "C":
    tempo.pop(-1)


    def convert(list):
        s = [str(i) for i in list]
        res = int("".join(s))
        return (res)


    x = convert(tempo)
    f = (x * 9) / 5 + 32
    print(f,"F")
else:
    print("Invalid Input")

