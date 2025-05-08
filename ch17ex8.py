"""exercise 8: This exercise is a cautionary tale about a common error that can be difficult to debug. Consider the
following class definition."""

"""
A Kangaroo is a marsupial.

__init__ takes two parameters: name is required, but contents is optional – if it’s not provided, the default value is an empty list.

__str__ returns a string representation of the object that includes the name and the contents of the pouch.

put_in_pouch takes any object and appends it to contents.

We create two Kangaroo objects with the names 'Kanga' and 'Roo'.

To Kanga’s pouch we add two strings and Roo.

If we print Kanga, it seems like everything worked.

But if we print Roo, we see that Roo’s pouch contains the same items as Kanga’s.

Write code to fix this bug.
"""

class Kangaroo:
    """A Kangaroo is a marsupial."""

    def __init__(self, name, contents=None):
        """Initialize the pouch contents.

        name: string
        contents: initial pouch contents.
        """
        self.name = name
        if contents is None:
            self.contents = []
        else:
            self.contents = contents

    def __str__(self):
        """Return a string representation of this Kangaroo."""
        t = [self.name + ' has pouch contents:']
        for obj in self.contents:
            t.append('    ' + str(obj))
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.

        item: object to be added
        """
        self.contents.append(item)


# Example test code
kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')

kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)
print()
print(roo)

