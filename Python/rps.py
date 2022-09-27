#Jamison Talley
#4-12-21
#rps.py
import random

#explains rules and initializes variables
print("Enter rock, paper, or scissors to test your might!")
print("(Enter q to quit)")
move_index = ["rock","paper","scissors"]
last_move = "i"
last_turn = "i"
user_input = str(input())
cont = True

#main game loop
while cont == True:
    #seperates inputs (error management)
    if user_input in move_index:
        #decides the computer's move
        if last_turn == "i":
            cpu_move = random.randint(0,2)
        elif (last_turn == "cpu") or (last_turn == "draw"):
            cpu_move = (cpu_move + 1) % 3
        elif last_turn == "user":
            cpu_move = (cpu_move - 1) % 3
        user_move = move_index.index(user_input)
        cpu_output = move_index[cpu_move]
        print(cpu_output)
        
        
        #decides win condition of current move and
        #prints the winner accordingly
        if cpu_move == user_move:
            last_turn = "draw"
        elif (cpu_move - user_move) == -2:
            last_turn = "cpu"
        elif (cpu_move - user_move) == -1:
            last_turn = "user"
        elif (cpu_move - user_move) == 1:
            last_turn = "cpu"
        elif (cpu_move - user_move) == 2:
            last_turn = "user"
        if last_turn == "user":
            print("You Win!")
        elif last_turn == "cpu":
            print("You Lose!")
        else:
            print("Draw!")
        
        user_input = input()

    #creates a case for the user to exit the game
    elif user_input == "q":
        cont = False
        print("Thanks for playing!")

    #handles formatting errors
    else:
        print("Oops... there seems to have been an error...")
        cont_val = input("Would you like to try again?\n")
        if cont_val == "yes":
            user_input = str(input())
            cont = True
        else:
            cont = False
            print("Thanks for playing!")

#Note the 'cpu' for this program does not rely on purely random
#methods to decide upon a move. The strategy is based on standard
#rock/paper/scissors theory, and thus is expected to have a greater
#than 50% chance at winning in the long run when playing against an
#average human