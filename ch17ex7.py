"""exercise 7: A hand has a full house if it contains three cards of one rank and two cards of another rank. Write a
PokerHand method that checks whether a hand has a full house"""


import random

class Card:
    """Represents a standard playing card."""

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


class Deck:
    """Represents a deck of playing cards."""

    def __init__(self, cards):
        self.cards = cards

    @staticmethod
    def make_cards():
        cards = []
        for suit in range(4):
            for rank in range(2, 15):
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
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.label = label
        self.cards = []


class PokerHand(Hand):
    """Represents a poker hand."""

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
        """Returns True if hand has a flush (5 or more of same suit)."""
        suit_counts = self.get_suit_counts()
        return any(count >= 5 for count in suit_counts.values())

    def has_straight(self):
        """Returns True if hand has a straight (5 consecutive ranks)."""
        ranks = set(card.rank for card in self.cards)

        if 14 in ranks:
            ranks.add(1)

        sorted_ranks = sorted(ranks)
        count = 0

        for i in range(len(sorted_ranks)):
            if i > 0 and sorted_ranks[i] == sorted_ranks[i - 1] + 1:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0
        return False

    def has_straight_flush(self):
        """Returns True if hand has a straight flush (5 consecutive ranks in same suit)."""
        suits = set(card.suit for card in self.cards)
        for suit in suits:
            suited_ranks = set(card.rank for card in self.cards if card.suit == suit)

            if 14 in suited_ranks:
                suited_ranks.add(1)

            sorted_ranks = sorted(suited_ranks)
            count = 0

            for i in range(len(sorted_ranks)):
                if i > 0 and sorted_ranks[i] == sorted_ranks[i - 1] + 1:
                    count += 1
                    if count >= 4:
                        return True
                else:
                    count = 0
        return False

    def has_pair(self):
        """rtrns True if hand has a pair (two or more cards with same rank)."""
        rank_counts = self.get_rank_counts()
        return any(count >= 2 for count in rank_counts.values())

    def has_full_house(self):
        """rtrns True if hand has a full house (three of one rank and two of another)."""
        rank_counts = self.get_rank_counts().values()
        has_three = 3 in rank_counts
        has_two = 2 in rank_counts
        return has_three and has_two

hand = PokerHand()
hand.cards = [Card(0, 2), Card(1, 2), Card(2, 2), Card(0, 3), Card(1, 3)]
print(hand)
print("Full house?", hand.has_full_house())  # should be True

