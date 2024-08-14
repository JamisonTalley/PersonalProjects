#Jamison Talley
#4-18-2022
#player.py

#imports necessary modules
from card import Card
from deck import Deck

#creates a data type "Player" that stores information about
#any players in the game
class Player:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._hand = []
        return
    
    #funciton returns the player's hand
    def get_hand(self):
        return self._hand

    #function prints the player's hand
    def print_hand(self):
        for i1 in range(len(self._hand)):
            print(self._hand[i1])
        return
    
    #function prints the first card in the player's hand
    def print_first(self):
        print(self._hand[0])
        return

    #funciton resets the hand of the player variable
    def clear(self):
        self._hand = []
        return

    #function adds a card to the player's hand from a given deck
    def deal(self, deck):
        self._hand.append(deck.deal())
        return
    
    #function prints the player's balance
    def print_balance(self):
        print(self._balance)
        return

    #function returns the player's balance
    def get_balance(self):
        return self._balance

    #function removes a given amount from the player's balance if possible
    def bet(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False

    #adds a given amount to the player's balance
    def win(self, amount):
        self._balance += float(amount)
        return

    #returns the value of the player's hand in blackjack scoring
    def blackjack_hand_value(self):
        hand_val = 0
        for i1 in range(len(self._hand)):
            hand_val += self._hand[i1].get_value()
        return hand_val

    #returns true if the blackjack value of the player's hand is 21
    def blackjack(self):
        if self.blackjack_hand_value() == 21:
            return True
        else:
            return False
    
#establishes a test client
if __name__ == "__main__":
    my_player = Player("Bob", 100)
    my_deck = Deck()
    my_player.deal(my_deck)
    my_player.print_balance()
    my_player.print_first()
    my_player.print_hand()
    print(my_player.bet(50))
    my_player.win(75)
    my_player.print_balance()
    print(my_player.blackjack_hand_value())
    print(my_player.blackjack())