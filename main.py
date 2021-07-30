# Rock Paper Scissors
# V1.0
# Imports
import random
import pyfiglet as pf

#banner
def print_banner():
    banner = pf.figlet_format("Rock Paper Scissors")
    print(banner)


# print welcome message
def print_welcome_message():
    welcome_message = "Welcome to Rock, Paper, Scissors v1.0. "
    instructions = "First to 3 points wins. Good Luck!"
    copyright = "(c) Someone in China. 206 BCE – 220 CE\n"
    print(copyright)
    print(welcome_message, instructions)


# check who won
def check_guess(usr_guess, cpu_guess):
    if usr_guess == "rock" and cpu_guess == "paper":
        return True
    elif usr_guess == "paper" and cpu_guess == "rock":
        return False
    elif usr_guess == "scissors" and cpu_guess == "rock":
        return True
    elif usr_guess == "rock" and cpu_guess == "scissors":
        return False
    elif usr_guess == "paper" and cpu_guess == "scissors":
        return True
    elif usr_guess == "scissors" and cpu_guess == "paper":
        return False


# game script
guesses = ["rock", "paper", "scissors"]
game_count = 0
cpu_wins = 0
usr_wins = 0
cpu_guess = ""
usr_guess = ""
# play_again = True

print_banner()
print_welcome_message()
# while play_again == True:

while cpu_wins < 3 and usr_wins < 3:
    print("Game:", game_count + 1, "\n~~~~~~~")
    usr_guess = input("Please enter your guess (rock, paper, scissors): ")
    usr_guess.lower()
    while usr_guess.lower() not in guesses:
        usr_guess = input("Sorry, I didn't catch that. Enter again: ")
    cpu_guess = random.choice(guesses)
    print(". \n. \n. \n")
    print("CPU guesses: ", cpu_guess.title(), "\n")
    if check_guess(usr_guess, cpu_guess) == True:
        print("{} beats {}. CPU wins.\n".format(cpu_guess.title(), usr_guess.title()))
        cpu_wins += 1
    elif check_guess(usr_guess, cpu_guess) == False:
        print("{} beats {}. You win.\n".format(usr_guess.title(), cpu_guess.title()))
        usr_wins += 1
    else:
        print("It's a tie:/\n")
    print("SCORE: CPU {} | USER {}\n".format(cpu_wins, usr_wins))
    game_count += 1

    if cpu_wins >= 3:
        go = pf.figlet_format(("Game Over! GG"))
        print(go)
        print("CPU Wins :(")
        print("Better luck next time")

    elif usr_wins >= 3:
        winner = pf.figlet_format("WINNER!")
        print(winner)
        print("Congratulations!")
        print("You win! :)")
# else:
#     again = input("Play again? (y/n): ")
#     if again.lower() == "y":
#         cpu_wins = 0
#         usr_wins = 0
#         game_count = 0
#         play_again = True

