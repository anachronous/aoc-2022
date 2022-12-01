# get input from file inputday1.txt
inputfile = open("C:\\GitHub\\aoc-2022\\Day 1\\inputday1.txt", "r")

# create list to save the highest calories for each elf
highestcalories = []
# variable to hold the amount of calories of an elf, will be reset once a new one appears
calories = 0

# read the input file
for line in inputfile:

    # if the line is empty, save the calories to highestcalories and reset the calories
    if (line == "\n"):
        # save calories to the list
        highestcalories.append(calories)
        # set calories back to 0
        calories = 0

    # if the line is not empty, add the calories to the total
    else:
        calories += int(line)

######## Part 1 ########

# print the highest number of calories in highestcalories
print("Part 1: " + str(max(highestcalories)))

######## Part 2 ########

# print the sum of the highest 3 numbers in highestcalories
highestcalories.sort(reverse=True)
print("Part 2: " + str(highestcalories[0] + highestcalories[1] + highestcalories[2]))