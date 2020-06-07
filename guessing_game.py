"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print("""
--------------------------------------
Welcome to the number guessing game!!!
--------------------------------------
""")

    
    while True:
        counter = 1
        rand = random.randint(1, 10)
        guess = int(input("Pick a number between 1 and 10: "))
        
        
        while guess > 10:
            guess = int(input("That is outside the number range. Please try agian: "))
        
        
        if guess != rand:
            counter += 1
            if guess < rand:
                print("It's higher")
            elif guess > rand:
                print("It's lower")
            guess = int(input("Pick a number between 1 and 10: "))
            
            
        else:
            print("You got it! It took you {} tries.".format(counter))
        play_agian = input("You won! Would you like to play agian? [y]es/[n]o: ")
        if play_agian != 'y':
            print("\n\nClosing game, see you next time!")
            break
            
            
        else:
            high_score(counter, high)
            continue
            
            
high = 10
def high_score(points, high):
    if points < high:
        high = points
    print("The HIGHSCORE is {}".format(high))
        
            
    
    
        
        
     

# Kick off the program by calling the start_game function.
start_game()