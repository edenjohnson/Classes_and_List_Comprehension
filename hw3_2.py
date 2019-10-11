###############################################################################
# hw3_2.py
# Author: Eden Johnson
# Last Modified: 10/10/19
# Purpose: Write a object-oriented program that contains two classes, Deck and
#          Card. To create a deck of card object, you need to write a class 
#          called "Deck" using requirements, and it should use another class
#          called "Card". 
# Program Uses: Built-in Python functions len(), print(), range(). built-in
#               Python methods .append(), .format(), .remove(). Use of class
#               creation with attributes and methods, import of the random
#               module and use of its shuffle() method, list comprehension.
###############################################################################

import random

class Card:
    def __init__(self, value, suit):
        """ Constructor to initialize class Card attributes. """
        self.value = value      # A,2,3,4,5,6,7,8,9,10,J,Q, or K
        self.suit = suit        # hearts, diamonds, clubs, spades

class Deck:
    def __init__(self, list_of_cards):
        """ Constructor to initialize class Deck attributes that overrides
            Card class __init__ method. """
        self.list_of_cards = list_of_cards
        
    def shuffle(self):
        """ Shuffle method should shuffle the full 52 card deck randomly. """
        if len(self.list_of_cards) == 52:
            random.shuffle(self.list_of_cards)
        else:
            print("The size of your deck is {}"\
                  .format(len(self.list_of_cards)) + \
                  " and is not big enough to shuffle.\n")
        
    def deal(self):
        """ Method should deal a single card from the deck and remove
            the card from the deck after it is dealt. """
        card_deal = 0
        for card in self.list_of_cards:
            if card_deal == 0:
                card_deal += 1
                print("You have been dealt the {} ".format(card.value) \
                       + "of {}.".format(card.suit) + "\n")
                # delete the card from the deck after it has been dealt
                self.list_of_cards.remove(card)   
            
value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suit =  ['Hearts','Diamonds','Clubs','Spades']

# create list of all 52 Card objects using list comprehension
deck_list = [Card(value[j], suit[i]) for i in range(len(suit))\
            for j in range(len(value))]

# create the Deck
deck = Deck(deck_list)

# shuffle the deck, deal cards
deck.shuffle()
deck.deal()
deck.shuffle()
deck.deal()
deck.shuffle()

        
