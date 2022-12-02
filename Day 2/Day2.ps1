# read input
$files = Get-Content -Path "C:\GitHub\aoc-2022\Day 2\inputday2.txt"

# the various values
$rock = 1
$paper = 2
$scissors = 3
$score = 0
$scorept2 = 0

# iterate over each line
ForEach ($file in $files) {
    # split the line into an array
    $matchup = $file -split " "
    
    # then points depending on what we chose
    if ($matchup[1] -eq "X") { 
        # rock
        $score += $rock 

        # check if opponent is scissors
        if ($matchup[0] -eq "C") { 
            $score += 6 
            $scorept2 += $paper
        }

        # check if opponent is rock
        if ($matchup[0] -eq "A") { 
            $score += 3 
            $scorept2 += $scissors
        }

        # check if opponent is paper
        if ($matchup[0] -eq "B") {
            $scorept2 += $rock
        }
    } 

    if ($matchup[1] -eq "Y") { 
        # paper
        $score += $paper 

        # check if opponent is rock
        if ($matchup[0] -eq "A") { 
            $score += 6 
            $scorept2 += ($rock + 3)
        }

        # check if opponent is paper
        if ($matchup[0] -eq "B") { 
            $score += 3
            $scorept2 += ($paper + 3)
         }

        # check if opponent is scissors
        if ($matchup[0] -eq "C") {
            $scorept2 += ($scissors + 3)
        }
    }

    if ($matchup[1] -eq "Z") { 
        # scissors
        $score += $scissors 

        # check if opponent is paper
        if ($matchup[0] -eq "B") { 
            $score += 6 
            $scorept2 += ($scissors + 6)
        }

        # check if opponent is scissors
        if ($matchup[0] -eq "C") { 
            $score += 3 
            $scorept2 += ($rock + 6)
        }

        # check if opponent is rock
        if ($matchup[0] -eq "A") {
            $scorept2 += ($paper + 6)
        }
    }
}

###### Part 1 ######

Write-Host $score -ForegroundColor Blue -BackgroundColor White

###### Part 2 ######

Write-Host $scorept2 -ForegroundColor Green -BackgroundColor White