#!python3
import random

ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
suits = ['H','C','S','D']

deck = [f"{j}{i}" for i in suits for j in ranks]
print("The first five cards are: ",deck[0],deck[1],deck[2],deck[2],deck[3])
z = round(len(deck)/2)
fdeck = deck[0:z]
sdeck = deck[z:]
sdeck.reverse()

deck = fdeck+sdeck
print("The sorted deck is", deck)

def shuffle(deck):
    random.shuffle(deck)
    return deck

def deal(deck):
    ask = int(input("How many cards would you like to deal?\n"))
    hand = []

    for i in range(ask):
        hand.append(deck[0])
        deck.pop(0)
    print("You hand is:", hand)


shuffle(deck)
deal(deck)
