# get input from inputday4.txt
inputfile = open("E:\\github repos\\aoc-2022\\Day 4\\inputday4.txt", "r")

# variable to save the result
resultPart1 = 0
# another one for part 2
resultPart2 = 0

######## Helper Functions ########

# define a function to check if the assignment pair contains each other
def does_contain(left1, right1, left2, right2):
    return (left1 <= left2 and right1 >= right2) or (left1 >= left2 and right1 <= right2)

# check if the assignment overlaps at all
def does_overlap(left1, right1, left2, right2):
    return (left1 <= left2 and right1 >= left2) or (left2 <= left1 and right2 >= left1)

######## Main ########

# iterate over inputfile
for line in inputfile:
    # split line into left and right
    left, right = line.split(",")
    # further split left and right into left1, right1 and left2, right2 respectively
    left1, right1 = left.split("-")
    left2, right2 = right.split("-")
    # convert left1, right1, left2, right2 to int
    left1 = int(left1)
    right1 = int(right1)
    left2 = int(left2)
    right2 = int(right2)

    # check if one of the ranges contains the others
    if does_contain(left1, right1, left2, right2):
        # if yes, increment res
        resultPart1 += 1
    
    # check if they overlap
    if does_overlap(left1, right1, left2, right2):
        resultPart2 += 1

######## Part 1 ########

# print resultPart1 without changes
print(resultPart1)

######## Part 2 ########

# print resultPart2 without changes
print(resultPart2)
