from random import randint
import time 
import sys
import os

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.004)

delay_print("What is your name: ")
name = input()

name = name.replace(' ','')

if name == '':
    name = 'Player_One'    
computer_score = 0
player_score = 0
rule = 0
no = 0
none = 0
t = 0
rules = '''
Welcome to rockpaper.py, a simple game of rock paper scissors.

The rules are simple. You will choose either a rock, paper, or scissors.
Simultaneously, I will randomly choose a guess as well.
Then we will compare.

Scissors always beats paper. Paper always beats rock. Rock always beat scissors. 

If you would like to play, please enter 'yes'. 
If not, please respectfully enter a 'no', and be on your merry way.

'''

info = '''
yes = play
no = do not play

Enter 'rules' if you would like to know the rules.

'''

delay_print("Hello, " + name + "!\nWould you like to play a game of rock, paper, scissor? ")
choice = input() 
while True:
    while True:
        if choice.lower() == 'yes' or choice.lower() == 'y':
            break
        elif choice.lower() == 'no' or choice.lower() == 'n':
            delay_print("Too bad. Have a nice day, " + name + ".")
            print("\n")
            none = 1
            break
        elif choice.lower() == 'rules':
            if rule == 0:
                delay_print(rules)
                rule = 1
                choice = input()
                continue
            else:
                print(rules)
                choice = input()
                continue
        else:
            if no < 2:
                delay_print("Please give me a 'yes' or a 'no'. ")
                choice = input()
                no = no + 1
                continue 
            else:
                delay_print(info)
                choice = input()
                continue
    if none == 0:
        pass
    else:
        break
    while True:
        if t == 0:
            if sys.platform.startswith('win32'):
                os.system('cls')
            else:
                os.system('clear')
            t = 1
        else:
            print('\n')
        delay_print("Rock, paper, or scissors? ")
        player = input()

        if player.lower() == 'rock' or player.lower() == 'paper' or player.lower() == 'scissors' or player.lower() == 'r' or player.lower() == 'p' or player.lower() == 's' or player.lower() == 'scissor': 
            break
        else:
            print("!Please enter a valid input!")
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
    print("\n")
    delay_print(player.upper() + ' VS. ' + chosen.upper())
    print("\n")
    
    if player == chosen:
      delay_print("DRAW!")
      print(" \n")
    elif player == 'rock' and chosen == 'scissors':
      delay_print(name.upper() + ' WINS!')
      print("\n")
      player_score = player_score + 1
    elif player == 'scissors' and chosen == 'paper':
      delay_print(name.upper() + ' WINS!')
      print("\n")
      player_score = player_score + 1
    elif player == 'paper' and chosen == 'rock':
      delay_print(name.upper() + ' WINS!')
      print("\n")
      player_score = player_score + 1
    else:
        delay_print(name.upper() + ' LOSES!')
        computer_score = computer_score + 1
        print("\n")
    
    player_print_score = name + ': ' + str(player_score) 
    computer_print_score = "Computer: " + str(computer_score)
    scorecard = '\n' + player_print_score + '\n' + computer_print_score + '\n'
    
    print(scorecard)
    
    while True:
        delay_print("Would you like to play again? ")
        play = input()
    
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
        elif play.lower() == 'credit':
            delay_print("\n\n'Written with love'\n\n\n- ballerboyer\n\n")
            continue
        else:
            print("Please enter 'yes' or 'no'.") 
            continue
  
    if play.lower() == 'yes':
        continue
  
    else:
        break

  