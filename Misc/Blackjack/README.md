This is my code for a fully interactive, object oriented version of the game blackjack.
This program works using nothing but Python's built in libraries and my own classes.
One of my points of emphasis in this project was reusability and readability of code. The classes in this program could very easily be reused for coding other card games, or card simulations.

The program is structured as follows:

blackjack.py
is the cumulative code behind the game, and uses the other three files
as libraries to run the game.

card.py
is the fundamental class in the program, and establishes the data
structure for the value of individual cards

deck.py
uses the Card class established by card.py to build a class for entire
decks of cards. 

player.py
uses the Card and Deck data types to establish a blackjack-specific
player class to manage player hands and balances.
