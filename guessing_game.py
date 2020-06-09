import random
high_score = 20


def start_game(h_score):
    print("-" * 38 + "\nWelcome to the number guessing game!!!\n" + "-" * 38)
    ran_num = random.randint(1, 10)
    counter = 1

    while True:        
        try:
            guess = int(input("\nPick a number between 1 and 10: "))
            if guess < 1 or 10 < guess:
                raise ValueError("That is an invalid value. Please try agian.")

        except ValueError as err:
            print("Your guess must be between 1 and 10.")
            print("{}".format(err))
            continue
        
        if guess != ran_num:
            counter += 1

            if guess < ran_num:
                print("It's higher")

            elif guess > ran_num:
                print("It's lower")
            
            continue

        if guess == ran_num:
            print("\nYou got it! It took you {} tries.".format(counter))
            play_agian = input("Winner! Would you like to play agian? [y]es/[n]o: ")
            if h_score > counter:
                h_score = counter
            print("\nThe high score is {}.\n".format(h_score))
                
            if play_agian.lower() == 'y':
                start_game(h_score)
                
            else:
                print("\nClosing game. Thanks for playing.\n")
                
             
        break    

start_game(high_score)