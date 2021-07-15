# import the random function to generate a random number
import random

# A list/array of response options that the computer can select from (0-2)
options = ["rock", "paper", "scissors"]

# The first to reach this score will win the game
winning_score = 3

# The scores for the player and the computer
player_score = 0
computer_score = 0

# This loop will continue until either the player or computer has reached the winning score
while player_score < winning_score and computer_score < winning_score:

    # Instruct the user on what to input
    user_response = input("Enter Rock, Paper, or Scissors: \n")

    # The computer will generate a number from 0-2 then grab that value from the options list/array
    computer_response = options[random.randint(0, 2)]

    # Announce the responses from the user and the computer
    print(f'Player chose {user_response}. Computer chose {computer_response}\n')

#This is the conditions for the game.
    if user_response == "rock" and computer_response == "paper":
        print(f"{computer_response}, Computer has won this match")
        computer_score += 1
    elif user_response == "paper" and computer_response == "rock":
        print(f"{user_response}, Player has won this match")
        player_score += 1
    elif user_response == "scissors" and computer_response == "scissors":
        print("Draw, no one won this match")
    elif user_response == "rock" and computer_response == "rock":
        print("Draw, no one won this match")
    elif user_response == "paper" and computer_response == "paper":
        print("Draw, no one won this match")
    elif user_response == "scissors" and computer_response == "rock":
        print(f"{computer_response} , Computer has won this match")
        computer_score += 1
    elif user_response == "rock" and computer_response == "scissors":
        print(f"{user_response}, Player has won this match")
        player_score += 1
    elif user_response == "paper" and computer_response == "scissors":
        print(f"{computer_response}, Computer has won this match")
        computer_score += 1
    elif user_response == "scissors" and computer_response == "paper":
        print(f"{user_response}, Player has won this match")
        player_score += 1
    print ("\n--------------------------\n")

# After someone has won, we will print "You have won!" to the screen
if player_score == winning_score:
    print("\n\nPlayer has won")
else:
    print("\n\nComputer has won")

# Pseudocode
# ---------------
# #Game Counts
# count_game=0
# while count_game<3:
#  print(count_game)
# Setup the logic with if else statements

# If Kel choose scissors and Lor choose scissors
# print draw
# If Kel choose rock and Lor choose rock
# print draw
# If Kel choose paper and Lor choose paper
# print draw
# If Kel choose scissors and Lor choose rock
# print rock
# If Kel choose rock and Lor choose scissors
# print rock
# If Kel choose paper and Lor choose scissors
# print scissors
# If Kel choose scissors and Lor choose paper
# print scissors
#
#
