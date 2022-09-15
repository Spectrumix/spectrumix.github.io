import random
from secrets import choice #importing random libary


def get_choices(): # creating a function with no input parameters
    player_choice = input("Enter a choice (rock , paper or scissors): ") # player import  and text information
    options = ["rock", "paper", "scissors"] # variable with 3 string objects/values
    computer_choice = random.choice(options) # applying the random function to the [options]
    choices = {"player": player_choice, "computer": computer_choice} # dictionary with 2 keys (player and comupter) , with its assgined object
    return choices #  returns the dictonary variable choices

def check_win(player, computer): # creating a function with 2 input parameters
    print(f"You chose {player} and computer chose {computer}.") # f string enablees bothe string and variables in print statments
    if player == computer: # condtional statments if both values are equal
        return "Its's a tie!" # returns text stating the last condition is true
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes sciessors! You win!"
        else: # no need for [if computer == "paper"] because it is the only option left, [ if computer == "rock"] it would already be equal to player resulting in a tie above
            return "Paper covers rock! You lose"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else: # same as above but for paper from player
            return "Scissors cuts paper! You lose"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
         return "Rock smashes scissors! You lose"
    else:
        return "i dont think thats an option!?"


choices = get_choices() # assgins the function created earlier to an object
result = check_win(choices["player"],choices["computer"]) # applys the check_wins function calling the "player" & "computer" keywords
#                                                                    to locate the values for [choices] within the get_chocies function
print(result)