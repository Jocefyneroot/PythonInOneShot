import random

compGuess = random.randint(1, 100)
# print(compGuess)

userScore = 0
while True:
    userGuess = int(input("Choose a Number between (1, 100): "))
    if userGuess > 100 or userGuess < 1:
        print("Enter Number between 1 to 100")
    elif compGuess == userGuess:
        print("****** Correct Guess ******")
        print(f"You Take {userScore} chance to Guess Correct One")
        print("Computer Guess:", compGuess)
        break
    elif userGuess > compGuess:
        print("Lower Number Please")
        userScore += 1
    else:
        print("Higher Number Please")
        userScore += 1
