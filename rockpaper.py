from random import randint
import time 
import sys
import os

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

name = str(input("What is your name: "))
name = name.replace(' ','')

if name == '':
    name = 'Player_1'
    
computer_score = 0
player_score = 0

while True:
    while True:
        player = input("Rock, paper, or scissors? ")

        if player.lower() == 'rock' or player.lower() == 'paper' or player.lower() == 'scissors' or player.lower() == 'r' or player.lower() == 'p' or player.lower() == 's' or player.lower() == 'scissor': 
            break
        else:
            print("Please enter a valid input")
            continue

    if player.lower() == 'r':
        player = 'rock'
    elif player.lower() == 'p':
        player = 'paper'
    elif player.lower() == 's':
        player = 'scissors'
    elif player.lower() == 'scissor':
        player = 'scissors'



    chosen = randint(1,3)

    if chosen == 1:
      chosen = 'rock'
    elif chosen == 2:
      chosen = 'paper'
    elif chosen == 3:
      chosen = 'scissors'

    print(player.upper() + ' VS. ' + chosen.upper())

    if player == chosen:
      delay_print("DRAW!")
      print(" ")

    elif player == 'rock' and chosen == 'scissors':
      delay_print(name.upper() + ' WINS!')
      print(" ")
      player_score = player_score + 1
    elif player == 'scissors' and chosen == 'paper':
      delay_print(name.upper() + ' WINS!')
      print(" ")
      player_score = player_score + 1
    elif player == 'paper' and chosen == 'rock':
      delay_print(name.upper() + ' WINS!')
      print(" ")
      player_score = player_score + 1
    elif chosen == 'rock' and player == 'scissors':
      delay_print(name.upper() + ' LOSES!')
      computer_score = computer_score + 1
      print(" ")
    elif chosen == 'scissors' and player == 'paper':
      delay_print(name.upper() + ' LOSES!')
      computer_score = computer_score + 1
      print(" ")
    elif chosen == 'paper' and player == 'rock':
      delay_print(name.upper() + ' LOSES!')
      computer_score = computer_score + 1
      print(" ")
    
    player_print_score = name + ': ' + str(player_score) 
    computer_print_score = "Computer: " + str(computer_score)
    scorecard = player_print_score + '\n' + computer_print_score
    
    print(scorecard)
    
    while True:
        play = input("Play again? ")
    
        if play.lower() == 'yes' or play.lower() == 'no':
            break
        elif play.lower() == 'score':
            print(scorecard)
            continue
        elif play.lower() == 'clear':
            if sys.platform.startswith('win32'):
                os.system('cls')
            else:
                os.system('clear')
        else:
            print("Please enter 'yes' or 'no'.") 
            continue
  
    if play.lower() == 'yes':
        continue
  
    else:
        break

  