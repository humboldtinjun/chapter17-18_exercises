"""exercise 2: “One of the exercises in Chapter 7 asks for a function called uses_none
 that takes a word and a string of forbidden letters, and returns True if the word
 does not use any of the letters. Here’s a solution: Write a version of this function
 that uses set operations instead of a for loop. Hint: ask a VA, 'How do I compute
 the intersection of Python sets?'"""

def uses_none(word, forbidden):
    return set(word.lower()).isdisjoint(set(forbidden.lower()))

# Test 
print(uses_none('hello', 'xyz'))  # True → no forbidden letters
print(uses_none('hello', 'lxz'))  # False → contains 'l'
print(uses_none('apple', 'pqr'))  # False → contains 'p'
print(uses_none('apple', 'xyz'))  # True → no forbidden letters
