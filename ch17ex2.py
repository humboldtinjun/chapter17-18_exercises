"""exercise 2: Write a Trick method called find_winner that loops through the cards in the Trick and returns the index
 of the card that wins. In the previous example, the index of the winning card is 2."""
class Card:
    """Represents a standard playing card."""

    # Class variables (shared by all cards)
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        rank_name = Card.rank_names[self.rank]
        suit_name = Card.suit_names[self.suit]
        return f'{rank_name} of {suit_name}'

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def to_tuple(self):
        return (self.suit, self.rank)

    def __lt__(self, other):
        return self.to_tuple() < other.to_tuple()

    def __le__(self, other):
        return self.to_tuple() <= other.to_tuple()


# 2️⃣ Deck class
import random

class Deck:
    """Represents a deck of playing cards."""

    def __init__(self, cards):
        self.cards = cards

    @staticmethod
    def make_cards():
        cards = []
        for suit in range(4):         # 0 to 3 → Clubs to Spades
            for rank in range(2, 15): # 2 to 14 → 2 to Ace
                card = Card(suit, rank)
                cards.append(card)
        return cards

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def take_card(self):
        return self.cards.pop()

    def put_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, other, num):
        for i in range(num):
            card = self.take_card()
            other.put_card(card)

class Trick(Deck):
    """reps a trick in contract bridge."""

    def find_winner(self):
        led_suit = self.cards[0].suit
        winning_index = 0
        winning_card = self.cards[0]

        for i, card in enumerate(self.cards[1:], start=1):
            if card.suit == led_suit and card.rank > winning_card.rank:
                winning_card = card
                winning_index = i
        return winning_index

cards = [Card(1, 3), Card(1, 10), Card(1, 12), Card(2, 13)]
trick = Trick(cards)
print(trick)
print("Winning index:", trick.find_winner())  # Should print 2

