"""exercise 7: Write a more concise version of this method with a list comprehension or generator expression."""

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = [
            Card('Hearts', 'A'),
            Card('Spades', 'K'),
            Card('Diamonds', 'Q'),
            Card('Clubs', 'J')
        ]
    def __str__(self):
        return '\n'.join(str(card) for card in self.cards)

# Test printing the deck
deck = Deck()
print(deck)
