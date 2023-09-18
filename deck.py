#!python3
import random

ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
suits = ['H','C','D','S']

deck = [f"{i} of {j}" for i in ranks for j in suits]
print(deck[0],deck[1],deck[2],deck[2],deck[3])

random.shuffle(deck)

ask = int(input("How many cards would you like to deal?\n"))
hand = []

for i in range(ask):
    hand.append(deck[0])
    deck.pop(0)

print(hand)
deck.sort()
print(deck)

for i in range(deck):
    if 

#HCDS
#a-k