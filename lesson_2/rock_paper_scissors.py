# First, the person selects Rock, Paper, Scissors
# Then, we random generate a number 1-3 to simulate a computer
# Compare the person's choice to the computer's and determine the winner

import random
VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
player_wins = 0
computer_wins = 0

def prompt(message):
    print(f'==> {message}')

def return_winner(player, computer):
    if ((player == 'rock' and computer == 'scissors') or
        (player == 'rock' and computer == 'lizard') or
        (player == 'paper' and computer == 'rock') or
        (player == 'paper' and computer == 'spock') or
        (player == 'scissors' and computer == 'paper') or
        (player == 'scissors' and computer == 'lizard') or
        (player == 'lizard' and computer == 'spock') or
        (player == 'lizard' and computer == 'paper') or
        (player == 'spock' and computer == 'rock') or
        (player == 'spock' and computer == 'scissors')):
        return 'Player wins'
    if((player == 'rock' and computer == 'spock') or
        (player == 'rock' and computer == 'paper') or
        (player == 'paper' and computer == 'scissors') or
        (player == 'paper' and computer == 'lizard') or
        (player == 'scissors' and computer == 'rock') or
        (player == 'scissors' and computer == 'spock') or
        (player == 'lizard' and computer == 'rock') or
        (player == 'lizard' and computer == 'scissors') or
        (player == 'spock' and computer == 'lizard') or
        (player == 'spock' and computer == 'paper')):
        return 'Computer wins'
    return 'Tie'

def display_winner (player, computer):
    if return_winner(player, computer) == 'Player wins':
        prompt('You win!')
    elif return_winner(player, computer) == 'Computer wins':
        prompt('You lose')
    else:
        prompt("It's a tie!")

def increment_winner (player, counter_1, computer, counter_2):
    if return_winner(player, computer) == 'Player wins':
        counter_1 += 1
    elif return_winner(player, computer) == 'Computer wins':
        counter_2 += 1
    else:
        print("You've tied! No change in the counter")
    return counter_1, counter_2

while True:
    #PERSON CHOOSES
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    #VALIDATE INPUT
    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    #COMPUTER CHOOSES
    computer_choice = random.choice(VALID_CHOICES)
    prompt(f'You chose {choice} and the computer chose {computer_choice}')

    #DETERMINE WINNER
    display_winner(choice, computer_choice)

    #INCREMENT WINNER
    player_wins, computer_wins = increment_winner(choice, player_wins, computer_choice, computer_wins)

    if player_wins > 2 or computer_wins >2:
        break

    prompt(f"""Current score:
           player has {player_wins} wins, 
           computer has{computer_wins} wins""")
    prompt('Do you want to play again (y/n)?')
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt('Please enter "y" or "n"')
        answer = input().lower()
    if answer[0] == 'n':
        break