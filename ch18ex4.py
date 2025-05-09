"""exercise 4: In one of the exercises from Chapter 17, my solution to
has_straightflush uses the following method, which partitions a PokerHand into a
list of four hands, where each hand contains cards of the same suit:

def partition(self):
    hands = []
    for i in range(4):
        hands.append(PokerHand())
    for card in self.cards:
        hands[card.suit].add_card(card)
    return hands

"""
from collections import defaultdict

# dummy classes
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __repr__(self):
        return f'{self.rank} of Suit {self.suit}'

class PokerHand:
    def __init__(self):
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
    def __repr__(self):
        return ', '.join(str(card) for card in self.cards)

# function using defaultdict
def partition(cards):
    hands = defaultdict(PokerHand)
    for card in cards:
        hands[card.suit].add_card(card)
    return hands

# Test data
cards = [
    Card(0, 'A'), Card(1, 'K'), Card(0, 'Q'),
    Card(2, 'J'), Card(1, '10'), Card(3, '9')
]

# Partition cards by suit
hands = partition(cards)

# Print out each hand
for suit, hand in hands.items():
    print(f'Suit {suit}: {hand}')

