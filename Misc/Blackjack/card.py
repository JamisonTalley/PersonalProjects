#Jamison Talley
#4-18-2022
#card.py


#creates a data type "Card" that stores the information
#on a typical playing card
class Card:
    def __init__(self, suit, face, value):
        self._suit = suit
        self._face = face
        self._value = value

    #function returns the value of the card
    def get_value(self):
        return self._value

    #function allows for the alteration of a cards value
    def set_value(self, value):
        self._value = value
        return

    #establishes a string protocol
    def __str__(self):
        return (self._face + " of " + self._suit)

#establishes a test client
if __name__ == "__main__":
    print(Card("Spades", "Ace", 11))