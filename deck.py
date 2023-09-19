#!python3
import random

ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
suits = ['H','C','S','D']
banned = []

deck = [f"{j}{i}" for i in suits for j in ranks]
print(deck[0],deck[1],deck[2],deck[2],deck[3])
fdeck = deck[]
sdeck = deck[]



def shuffle(deck):
    random.shuffle(deck)
    for i in banned:
        deck.pop(i)
    return deck

def deal(deck):
    ask = int(input("How many cards would you like to deal?\n"))
    hand = []

    for i in range(ask):
        hand.append(deck[0])
        banned.append(deck[0])
        deck.pop(0)

print(hand)
print(deck)


#HCDS
#a-k