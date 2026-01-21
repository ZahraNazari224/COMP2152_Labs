import random

# This is the python file for week02

choices=["Rock", "Papper", "Scissors"]
playerChoice=int(input("Enter your choice (1=Rock, 2=Paper, 3=Scissors): "))


if playerChoice <1 or playerChoice >3:
    print("Error: Choice must be between 1 and 3!")
else:
    computerChoice = random.randint(1,3)    
        
    playerChoiceIndex = choices[playerChoice - 1]
    computerChoiceIndex = choices[computerChoice - 1]


    print("You chose: ", playerChoiceIndex)
    print("Computer chose: ", computerChoiceIndex)
    
    # Determining the winner with if/elif/else
    if playerChoice == computerChoice:
        print("It's a tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("Rock beats scissors - YOU WIN!")
    elif playerChoice == 2 and computerChoice== 1:
        print("Paper beats Rock - You Win!")
    elif playerChoice == 3 and computerChoice == 2:
        print("Scissors beats paper - You Win!")
    else: print("You Lost!")
