data = []
with open("code.txt", "r") as file:
    for line in file : data.append(line.strip())
    total = 0
    for bank in data:
        bank = str(bank)
        first = 0
        for i in range(len(bank)):
            if int(bank[i]) > first:
                first = int(bank[i])
                index = i
        second = 0
        if index == 99:
            second = first
            first = 0
            for i in range(len(bank)-1):
                if int (bank[i]) > first : first = int(bank[i])
        else:
            for i in range(index+1,len(bank)):
                if int(bank[i]) > second : second = int(bank[i])
        total += int(str(first) + str(second))
print(total)