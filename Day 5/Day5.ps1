# read from file
$files = Get-Content -Path "C:\GitHub\aoc-2022\Day 5\inputday5.txt"

# create 9 stacks
$stack1 = @()
$stack2 = @()
$stack3 = @()
$stack4 = @()
$stack5 = @()
$stack6 = @()
$stack7 = @()
$stack8 = @()
$stack9 = @()

# push the starting values onto the stacks
$stack1.Push($J)
$stack1.Push($H)
$stack1.Push($G)
$stack1.Push($M)
$stack1.push($Z)
$stack1.push($N)
$stack1.push($T)
$stack1.push($F)

$stack2.Push($V)
$stack2.Push($W)
$stack2.Push($J)

$stack3.Push($J)
$stack3.Push($H)
$stack3.Push($G)
$stack3.Push($M)
$stack3.push($Z)
$stack3.push($N)
$stack3.push($T)

# iterate over each line
ForEach ($file in $files) {
    
}