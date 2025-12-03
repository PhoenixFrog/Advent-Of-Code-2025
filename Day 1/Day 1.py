sequence = []
magnitudes = []
with open("code.txt", "r") as file:
    for line in file:sequence.append(line.strip())
for number in sequence:
    absolute = int(number[1:])
    if number[0] == "L" : absolute = -1*absolute
    magnitudes.append(absolute)
place = 50
zeros = 0
for value in magnitudes:
    while value > 100 : value -= 100
    while value < -100 : value += 100
    place += value
    if place >= 100 : place -= 100
    elif place < 0 : place += 100
    elif place == 100 : place = 0
    if place == 0 : zeros += 1
print(zeros)