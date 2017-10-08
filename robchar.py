""" File for char class
is length one
chars are made and decided by the templates
used in charword for each char """

class robchar():

    def __init__(self, char, owner):
        """ char is the character that is
        owner is the charword or False """
        self.char = char
        self.owner = owner

    def ownedby(self):
        return self.owner

    def __str__(self):
        return self.char

    def string(self):
        return str(self.char)

    __repr__ = __str__