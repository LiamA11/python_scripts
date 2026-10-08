# Number guesser

import random

com = 0
player = 0
stop = "y"
turns = 0
highscore = 99999


print("Welcome to Number Guesser! I am thinking of a number between 1 and 100, try to guess which one in as few trys as possible.")
while stop.strip().lower() == "y":
    com = random.randint(1, 100)
    try:
        player = int(input("Make your first guess: "))
    except ValueError:
        print("Please enter a valid number!")
        continue
    turns = 1
    while com != player:
        turns += 1
        if com > player:
            player = int(input("Too low! Guess higher: "))
        elif com < player:
            player = int(input("Too high! Guess lower: "))

    if highscore > turns:
        highscore = turns
    
    print("Congrats! You found my number in", turns, "turns!")
    print("Your current highscore is", highscore)
    stop = str(input("Would you like to play again?(y/n): "))

print("Thanks for playing Number Guesser!\nYour final highscore is", highscore)
