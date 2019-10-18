###############################################################################
# hw3_2.py
# Author: Eden Johnson
# Last Modified: 10/18/19
# Purpose: Write a object-oriented program that contains two classes, Deck and
#          Card. To create a deck of card object, you need to write a class 
#          called "Deck" using requirements, and it should use another class
#          called "Card". 
# Program Uses: Built-in Python functions len(), print(), range(). built-in
#               Python methods .append(), .format(), .pop(). Use of class
#               creation with attributes and methods, import of the random
#               module and use of its shuffle() method, list comprehension.
###############################################################################

import random

# assign the values and suits for the deck of cards
value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suit =  ['Hearts','Diamonds','Clubs','Spades']

class Card:
    def __init__(self, value, suit):
        """ Constructor to initialize class Card attributes. """
        self.value = value      # A,2,3,4,5,6,7,8,9,10,J,Q, or K
        self.suit = suit        # hearts, diamonds, clubs, spades

class Deck:
    def __init__(self):
        """ Constructor to initialize class Deck attributes that overrides
            Card class __init__ method. """
        self.deck_of_cards = [Card(value[j], suit[i])\
                              for i in range(len(suit))\
                              for j in range(len(value))]
        
    def shuffle(self):
        """ Shuffle method should shuffle the full 52 card deck randomly. """
        if len(self.deck_of_cards) == 52:
            random.shuffle(self.deck_of_cards)
            print("Shuffling the full deck of cards..\n")
        else:
            print("The size of your deck is {}"\
                  .format(len(self.deck_of_cards)) + \
                  " and is not big enough to shuffle.\n")
        
    def deal(self):
        """ Method should deal a single card from the deck and remove
            the card from the deck after it is dealt. """
        dealt_card = self.deck_of_cards.pop()
        print("You have been dealt the {} ".format(dealt_card.value) \
                       + "of {}.".format(dealt_card.suit) + "\n")

# create the deck
deck = Deck()

# shuffle the deck, deal cards
deck.shuffle()
deck.deal()
deck.shuffle()
deck.deal()
deck.shuffle()

        
