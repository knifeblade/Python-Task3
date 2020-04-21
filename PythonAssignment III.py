# Random Guess Game

import random

user = input("Welcome Player! What is your name? ")
print(f"Hi {user}, It's time to try your guessing skills ")

game = "Random Guess Game "
print(game.upper())


def random_guess_game():

    start_game = True
    while start_game:
        hidden_easy = random.randint(1, 10)
        hidden_medium = random.randint(1, 20)
        hidden_hard = random.randint(1, 50)
        level_selection = int(input("Select Game Level: \nEnter '1' for Easy; Enter '2' for Medium; Enter '3' for Hard\n "))

        now_playing = True
        while now_playing:
            if level_selection == 1:
                print("Game level: Easy Mode Selected. You have 6 chances ")
                break
            if level_selection == 2:
                print("Game level: Medium Mode Selected. You have 4 chances")
                break
            if level_selection == 3:
                print("Game level: Hard Mode Selected. You have 3 chances")
                break
            else:
                print("Invalid selection! Please enter 1, 2, or 3")
                now_playing = not True
        if level_selection == 1:
            guess_count = 0
            guess_limit = 6
            while guess_count < guess_limit:
                user_input = input("Guess a number between 1 and 10: ")
                try:
                    guess = int(user_input)
                except ValueError:
                    print("Error! Please enter only numbers. Try again! ")
                    continue
                guess_count += 1
                chances = guess_limit - guess_count
                if guess == hidden_easy:
                    print("You got it right! ")
                    start_game = not True
                    break
                else:
                    print(f"That was wrong! You have only {chances} chances left ")
            else:
                if guess_count >= guess_limit:
                    print("Game Over!")
        elif level_selection == 2:
            guess_count = 0
            guess_limit = 4
            while guess_count < guess_limit:
                user_input = input("Guess a number between 1 and 20: ")
                try:
                    guess = int(user_input)
                except ValueError:
                    print("Error! Please enter only numbers. Try again! ")
                    continue
                guess_count += 1
                chances = guess_limit - guess_count
                if guess == hidden_medium:
                    print("You got it right! ")
                    break
                else:
                    print(f"That was wrong! You have only {chances} chances left ")
            else:
                if guess_count >= guess_limit:
                    print("Game Over!")
        elif level_selection == 3:
            guess_count = 0
            guess_limit = 3
            while guess_count < guess_limit:
                user_input = input("Guess a number between 1 and 50: ")
                try:
                    guess = int(user_input)
                except ValueError:
                    print("Error! Please enter only numbers. Try again! ")
                    continue
                guess_count += 1
                chances = guess_limit - guess_count
                if guess == hidden_hard:
                    print("You got it right! ")
                    break
                else:
                    print(f"That was wrong! You have only {chances} chances left ")
            else:
                if guess_count >= guess_limit:
                    print("Game Over!")
        play_again = True
        while play_again:
            replay = input("\nWould you like to play again?\nY or N\n ")
            if replay.upper() == "N":
                print("Nice game! Looking forward to our next play. ")
                play_again = not True
                start_game = not True
            elif replay.upper() == "Y":
                print("Okay Great! Let's play again!! ")
                play_again = not True
                start_game = True
            else:
                print("Invalid selection. Please enter Y or N ")
                play_again = not True
                start_game = not True


random_guess_game()
