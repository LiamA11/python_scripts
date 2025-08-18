# rock, paper, scissors
import random

com = "a"
player = "a"
choices = ("rock", "paper", "scissors")
stop = "y"
scoreC = 0
scoreP = 0

print("Rules: This game follows the basic rules of rock, paper, scissors. when the bot yells SHOOT, please type your turn.")

while stop.strip().lower() == "y":
    print("Rock... Paper... Scissors...")
    player = input("SHOOT: ").strip().lower()
    com = (random.choice(choices))
    print(com)
    if com == player:
        print("It's a tie!")
    elif player == "rock":
        if com == "paper":
            print("Hah, I win!")
            scoreC = scoreC + 1
        elif com == "scissors":
            print("Congrats, you win!")
            scoreP = scoreP + 1
    elif player == "paper":
        if com == "scissors":
            print("Hah, I win!")
            scoreC = scoreC + 1
        elif com == "rock":
            print("Congrats, you win!")
            scoreP = scoreP + 1
    elif player == "scissors":
        if com == "rock":
            print("Hah, I win!")
            scoreC = scoreC + 1
        elif com == "paper":
            print("Congrats, you win!")
            scoreP = scoreP + 1
    else:
        print("...Wait you've confused me.")
    
    print("The current score is", scoreC, "to", scoreP)
    stop = input("Would you like to play again?(y/n): ")

print("Thanks for playing!")