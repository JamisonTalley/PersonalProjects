#Jamison Talley
#4-18-2022
#deck.py

#imports necessary modules
import random
from card import Card

#creates a data type "Deck" that holds 52 shuffled cards
class Deck:
    def __init__(self):
        #creates a database from which to create the deck of cards
        suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        faces = ["Two", "Three", "Four", "Five", "Six","Seven",
                  "Eight", "Nine", "Ten", "Jack","Queen", "King", "Ace"]
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

        #initializes deck variables
        deck = []
        deck_rand = []

        #generates a card of all non-repeating combinations of the
        #suits and faces lists
        for i1 in range(4):
            for i2 in range(13):
                deck.append(Card(suits[i1], faces[i2], values[i2]))
        
        #draws from the unshuffled deck of cards to create a
        #shuffled deck of cards
        for i1 in range(52):
            rand_card = random.randint(0, len(deck) - 1)
            deck_rand.append(deck[rand_card])
            deck.remove(deck[rand_card])
        self._deck = deck_rand
    
    #function removes the top card from the deck and returns it
    def deal(self):
        deal = self._deck.pop()
        return deal
    
    #function returns the number of cards in the deck
    def deck_size(self):
        return len(self._deck)

    #function prints each card in the deck
    def print_deck(self):
        for i1 in range(len(self._deck)):
            print(self._deck[i1])
        return

#establishes a test client
if __name__ == "__main__":
    test_deck = Deck()
    test_deck.print_deck()
    print(test_deck.deck_size())
    print(test_deck.deal())
    print(test_deck.deck_size())

