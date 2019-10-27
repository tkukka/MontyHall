#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Monty Hall Problem
# https://en.wikipedia.org/wiki/Monty_Hall_problem
from random import shuffle, choice

GOAT = 0
CAR = 1
TEXT = ['goat', 'car']
N = 100000
prizes = [GOAT, GOAT, CAR]
doors = [0, 1, 2]


# Monty must pick any door that hides a goat
def monty_pick():
    s = set(doors)
    s2 = s - {pick}

    if prizes[pick] == CAR:
       #print(choice(list(s2)))
       return choice(list(s2))
   
    # Goat picked. Monty picks the other goat
    d = list(s2)
    
    if prizes[d[0]] == CAR:
        return d[1]
    
    return d[0]

def door_switch():
    s = set(doors) - {pick, mpick}
    #print(int(s.pop()))
    return int(s.pop())

print('Monty Hall problem. Iterations:', N)
thresh = int(N/10)
wins_stick = 0
wins_switch = 0
for i in range(N):

    if i % thresh == 0:
        print('.', end='')
    
    shuffle(prizes)
    pick = choice(doors)
    #print('Person picks a door #', pick, '. The prize not shown is a', TEXT[prizes[pick]])
    
    mpick = monty_pick()
    #print('Monty reveals a door #', mpick, '. The prize is a', TEXT[prizes[mpick]])
    
    # alternative choice
    pick2 = door_switch()

    if prizes[pick] == CAR:
        wins_stick += 1
        
    if prizes[pick2] == CAR:
        wins_switch += 1
       
print()
print('Wins by sticking with the door:', wins_stick, '(', 100*wins_stick/N, '%)')
print('Wins by changing your mind:', wins_switch, '(', 100*wins_switch/N, '%)')        
