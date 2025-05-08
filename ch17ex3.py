"""exercise 3: The next few exercises ask to you write functions
 that classify poker hands. If you are not familiar with poker, I’ll explain what
 you need to know. We’ll use the following class to represent poker hands."""

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


class Hand(Deck):
    """reps a hand of playing cards."""

    def __init__(self, label=''):
        self.label = label
        self.cards = []  # start empty (different from Deck's __init__)


class PokerHand(Hand):
    """reps a poker hdand."""

    def get_suit_counts(self):
        counter = {}
        for card in self.cards:
            key = card.suit
            counter[key] = counter.get(key, 0) + 1
        return counter

    def get_rank_counts(self):
        counter = {}
        for card in self.cards:
            key = card.rank
            counter[key] = counter.get(key, 0) + 1
        return counter

    def has_flush(self):
        """rtrns True if hand has a flush"""
        suit_counts = self.get_suit_counts()
        return any(count >= 5 for count in suit_counts.values())

deck = Deck(Deck.make_cards())
deck.shuffle()

hand = PokerHand()
deck.move_cards(hand, 7)  # deal 7 cards
print(hand)
print("Flush?", hand.has_flush())
