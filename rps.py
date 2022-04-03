import time
import random

num=5
for x in range(num):
    print(num)
    time.sleep(1)
    num-=1
print("Rock, paper, scissors!")

player_inp=input("Make Your Decision--> ")
option= random.choice(['Rock', 'Paper', 'Scissors'])
print(option)
if player_inp == option:
    print("Draw")
if player_inp == 'Rock' and option == 'Paper':
    print('Bot wins')
if player_inp == 'Paper' and option == 'Rock':
    print('You wins')
if player_inp == 'Scissors' and option == 'Paper':
    print('You wins')
if player_inp == 'Paper' and option == 'Scissors':
    print('Bot wins')
if player_inp == 'Rock' and option == 'Scissors':
    print('You wins')
if player_inp == 'Scissors' and option == 'Rock':
    print('Bot wins')