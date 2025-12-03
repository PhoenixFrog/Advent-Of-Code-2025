with open("code.txt", "r") as file : file = file.read()
sequences = file.split(",")
total = 0
for pair in sequences:
    pair = list(map(int, pair.split("-")))
    for i_d in range(pair[0], pair[1]+1):
        length = len(str(i_d))
        if length % 2 == 0:
            if str(i_d)[length//2:] == str(i_d)[:length//2] : total += i_d
print(total)