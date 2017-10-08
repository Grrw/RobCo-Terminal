""" File for the word class
is a certain length (to be used for curses displaying)
is composed of characters that are of char class """

class charword():

    def __init__(self, row, length):
        """
        """
        self.row = row
        self.length = length

    def rowturn(self):
        return self.row
