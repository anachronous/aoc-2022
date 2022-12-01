# get input from file inputday1.txt
inputfile = open("C:\\GitHub\\aoc-2022\\Day 1\\inputday1.txt", "r")

# create list
highestcalories = []
# variable to hold the amount of calories of an elf
calories = 0

# read the input file
for line in inputfile:

    # print(calories)
    # if the line is empty, save the calories to highestcalories and reset the calories
    if (line == "\n"):
        highestcalories.append(calories)
        calories = 0
    # if the line is not empty, add the calories to the total
    else:
        calories += int(line)

# print the highest number of calories in highestcalories
# print(max(highestcalories)) # part 1

# print the sum of the highest 3 numbers in highestcalories
highestcalories.sort(reverse=True)
print(highestcalories[0] + highestcalories[1] + highestcalories[2]) # part 2