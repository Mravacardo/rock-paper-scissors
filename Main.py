from tkinter import *
import tkinter.font as font
import random

player_score = 0
computer_score = 0
options = [('rock',0), ('paper',1), ('scissors',2)]

def computer_wins():
    global computer_score, player_score
    computer_score += 1
    winner_label.config(text="Computer Won!!!")
    computer_score_label.config(text='Computer Score : ' + str(computer_score))
    player_score_label.config(text='Player Score : ' + str(player_score))

def player_wins():
    global computer_score, player_score
    player_score += 1
    winner_label.config(text="Player Won!!!")
    computer_score_label.config(text='Computer Score : ' + str(computer_score))
    player_score_label.config(text='Player Score : ' + str(player_score))

def tie():
    global computer_score, player_score
    winner_label.config(text="Tie!!!")
    computer_score_label.config(text='Computer Score : ' + str(computer_score))
    player_score_label.config(text='Player Score : ' + str(player_score))

def player_choice(player_input):
    global computer_score, player_score
    print(player_input)

    computer_input = get_computer_choice()
    print(computer_input)
    player_choice_label.config(text = 'Your selected : ' + player_input[0])
    computer_choice_label.config(text = 'Computer selected : ' + computer_input[0])

    if player_input == computer_input:
        tie()

    if(player_input[1] == 0):
        if(computer_input[1] == 1)
            computer_wins()
        elif (computer_input[1] == 2):
            player_wins()

    elif(player_input[1] == 1):
        if(computer_input[1] == 0)
            player_wins()
        elif (computer_input[1] == 2):
            computer_wins()

    elif(player_input[1] == 2):
        if(computer_input[1] == 0)
            player_wins()
        elif (computer_input[1] == 2):
            computer_wins()

def get_computer_choice():
    return random.choice(options)

game_window = Tk()
game_window.title("Rock Paper Scissors Game")

app_font = font.Font(size = 12)

game_title = Label(text = 'Rock Paper Scissors', font = font.Font(size = 20), fg = 'grey')
game_title.pack()

winner_label = Label(text = "Lets Start the Game...", fg = 'green', font = font.Font)
