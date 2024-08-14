#Jamison Talley
#4-18-2022
#blackjack.py

#imports necessary modules
from card import Card
from deck import Deck
from player import Player

#intializes the shuffled deck we will be using
deck = Deck()

#obtains the necessary information through user input to 
#create the player variable, while using proper error analysis
print("What's your name?")
player_name = input()
print("How much money are you playing with today?")
balance = float(input())
while (balance <= 0):
    print("That's not a valid amount, try again")
    balance = float(input())

#begins the game and initializes the user and dealer players
print("Let's Play...")
player = Player(player_name, balance)
dealer = Player("dealer", 1000000)
play_again = True

#if the user chooses to keep playing, and has money to bet,
#the game will keep going in a loop
while (play_again == True) and (player.get_balance() >= 0):

    #reshuffles the deck if there are less than 20 cards left
    if deck.deck_size() < 20:
        deck = Deck()

    #obtains the players bet while using error management
    print("How much would you like to bet?")
    player_bet = float(input())
    while (player_bet <= 0) or (player_bet > player.get_balance()):
        print("Thats not a valid amount, try again")
        player_bet = float(input())

    player.bet(player_bet)

    #deals both the player and the dealer 2 cards
    player.deal(deck)
    dealer.deal(deck)
    player.deal(deck)
    dealer.deal(deck)

    #checks if the player or the dealer gets a natural
    if (player.blackjack() == True) and (dealer.blackjack() == False):
        move = "natural"
    elif (player.blackjack() == True) and (dealer.blackjack() == True):
        move = "push"
    elif (player.blackjack() == False) and (dealer.blackjack() == True):
        move = "loss"
    else:
        move = "hit"

    if "hit" in move:
        #displays the dealers upcards for the user
        print("\nThe dealer's upcards are: ")
        for i1 in range(1, len(dealer.get_hand())):
            print(dealer.get_hand()[i1])

        #displays the users hand
        print("\nYour hand: ")
        for i1 in range(len(player.get_hand())):
            print(player.get_hand()[i1])

        #allows the user to choose whether an ace is worth 1 or 11
        for i1 in range(len(player.get_hand())):
            if player.get_hand()[i1].get_value() == 11:
                print("Do you want your Ace to be worth 11 or 1?")
                if "11" not in input():
                    player.get_hand()[i1].set_value(1)

        #prompts the user to hit or stand
        print("\nhit or stand?")
        move = input().lower()

    while "hit" in move:

        #dealer stands on a soft 17
        player.deal(deck)
        if dealer.blackjack_hand_value() < 17:
            dealer.deal(deck)

        #displays the dealers upcards to the user
        print("\nThe dealer's upcards are: ")
        for i1 in range(1, len(dealer.get_hand())):
            print(dealer.get_hand()[i1])

        #displays the users hand
        print("\nYour hand: ")
        for i1 in range(len(player.get_hand())):
            print(player.get_hand()[i1])
        
        #allows the user to choose whether an ace is worth 1 or 11
        for i1 in range(len(player.get_hand())):
            if player.get_hand()[i1].get_value() == 11:
                print("Do you want your Ace to be worth 11 or 1?")
                if input() == "1":
                    player.get_hand()[i1].set_value(1)

        #checks a win condition during each round
        if (player.blackjack_hand_value() > 21) or (dealer.blackjack() == True):
            move = "loss"
        elif (player.blackjack() == True) or (dealer.blackjack_hand_value() > 21):
            move = "win"
        else:
            print("\nhit or stand?")
            move = input().lower()
            if "hit" in move:
                move = "hit"
            elif "stand" in move:
                move = "stand"

    #checks win condition if the user stands
    if move == "stand":
        if player.blackjack_hand_value() > dealer.blackjack_hand_value():
            move = "win"
        elif player.blackjack_hand_value() < dealer.blackjack_hand_value():
            move = "loss"
        elif player.blackjack_hand_value() == dealer.blackjack_hand_value():
            move = "push"
        else:
            move = "push"

    #displays the final value of the player's and dealer's hands
    print("\nThe dealer's hand: ")
    for i1 in range(len(dealer.get_hand())):
        print(dealer.get_hand()[i1])

    print("\nYour hand: ")
    for i1 in range(len(player.get_hand())):
        print(player.get_hand()[i1])
    print()

    #displays the win condition and distributes winnings if applicable
    if move == "natural":
        print("You Win!")
        player.win(2.5 * player_bet)
    elif move == "win":
        print("You Win!")
        player.win(2 * player_bet)
    elif move == "push":
        print("It's a tie")
        player.win(player_bet)
    elif move == "loss":
        print("You Lose")

    #resets variables for the next round
    player.clear()
    dealer.clear()

    #prompts the user to play another game or end
    print("\nYou have $", end="")
    print(player.get_balance(), end="")
    print(" left\n", end="")
    print("Play again?")
    if "yes" in input().lower():
        play_again = True
        move = "hit"
    else:
        play_again = False

print("Thanks for playing!")