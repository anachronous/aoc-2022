import time
startTime = time.time()

# get input from file inputday3.txt
inputfile = open("E:\\github repos\\aoc-2022\\Day 3\\inputday3.txt", "r")

# create variable to save the result for part 1
resultPart1 = 0
# and one for part 2
resultPart2 = 0

# create dictionary to map letters to numbers, starting with small letters, generated by copilot because i'm lazy
lettertonumber = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
# then add the capital letters, starting with 27, same here
lettertonumber.update({"A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46, "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52})

######## Part 1 ########

# read the input file
for line in inputfile:
    # get length of line
    linelength = len(line)

    # split line in half
    half1 = line[0:linelength//2]
    half2 = line[linelength//2:]
    # transform to set
    half1 = set(half1)
    half2 = set(half2)

    # iterate over half1
    for letter in half1:
        # check if the letter is also in half2
        if letter in half2:
            # if yes, add the corresponding value from lettertonumber to resultPart1
            resultPart1 += lettertonumber.get(letter)

# print resultPart1 without changes
print(resultPart1)

######## Part 2 ########

# get input from file inputday3.txt again, this time saving everything into a list
with open("E:\\github repos\\aoc-2022\\Day 3\\inputday3.txt", "r") as input:
    # get the lines
    lines = input.read().split("\n")
# save length of lines in advance
lineslength = len(lines)

# go over lines in intervals of 3
for i in range(0, lineslength-3, 3):
    # save current line to line1
    line1 = lines[i]
    # save next line to line2
    line2 = lines[i+1]
    # save the line after that to line3
    line3 = lines[i+2]

    # transform them all to sets
    line1 = set(line1)
    line2 = set(line2)
    line3 = set(line3)

    # iterate over line1
    for letter in line1:
        # check if the letter is in both line2 and line3
        if letter in line2 and letter in line3:
            # add the appropriate value to resultPart2
            resultPart2 += lettertonumber.get(letter)

# print resultPart2 without changes
print(resultPart2)

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))