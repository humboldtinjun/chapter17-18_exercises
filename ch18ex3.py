"""exercise 3: Scrabble is a board game where the objective is to use letter tiles
to spell words. For example, if we have tiles with the letters T, A, B, L, E, we can
spell BELT and LATE using a subset of the tiles – but we can’t spell BEET because
we don’t have two Es.

Write a function that takes a string of letters and a word, and checks whether
the letters can spell the word, taking into account how many times each letter
appears."""

from collections import Counter

def can_spell(tiles, word):
    tile_counter = Counter(tiles.lower())
    word_counter = Counter(word.lower())

    for letter in word_counter:
        if word_counter[letter] > tile_counter.get(letter, 0):
            return False
    return True

# Test cases
print(can_spell('table', 'belt'))   # True
print(can_spell('table', 'beet'))   # False
print(can_spell('table', 'late'))   # True
print(can_spell('table', 'teal'))   # True
print(can_spell('table', 'tablet')) # False
