
import random

from games.blackjack import create_deck

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

#====================================
balance = 100
bet = float(input("Wat wil je inzetten?"))
print(bet)
print()
balance -= bet
print(balance)
print()

#stap 2 deck maken
deck = []
for suit in SUITS:
    for rank in RANKS:
        deck.append(f"{suit}{rank}")
print(deck)
print(len(deck))

deck = ["♠A", "♥9", "♦K"]
card = deck.pop()
print(card)

player_hand = []
player_hand.append("♠A")
player_hand.append("♥8")
print(player_hand)
print (len(player_hand))

def draw_card(deck, hand):
    card = deck.pop()
    hand.append(card)
    return hand