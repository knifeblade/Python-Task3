# Random Guess Game

import random

user = input("Welcome Player! What is your name? ")
print(f"Hi {user}, It's time to try your guessing skills! ")


def random_guess_game():

    start_game = True
    while start_game:
        hidden_easy = random.randint(1, 10)
        hidden_medium = random.randint(1, 20)
        hidden_hard = random.randint(1, 50)
        level_select = input("Game Level: \nEnter '1' for Easy; Enter '2' for Medium; Enter '3' for Hard\n ")
        try:
            level_selection = int(level_select)
        except ValueError:
            print("Error! Please enter '1', '2' or '3'. ")
            continue
            
        now_playing = True
        while now_playing:
            if level_selection == 1:
                print("Game level: Easy Mode Selected. You have 6 chances. ")
                break
            if level_selection == 2:
                print("Game level: Medium Mode Selected. You have 4 chances. ")
                break
            if level_selection == 3:
                print("Game level: Hard Mode Selected. You have 3 chances. ")
                break
            else:
                print("Invalid selection! Try again! ")
                now_playing = not True
        if level_selection == 1:
            guess_count = 0
            guess_limit = 6
            while guess_count < guess_limit:
                user_input = input("\nGuess a number between 1 and 10: ")
                guess_count += 1
                chances = guess_limit - guess_count
                try:
                    guess = int(user_input)
                except ValueError:
                    print(f"Error! Please enter only numbers. You have {chances} chance(s) left. ")
                    continue
                if guess == hidden_easy:
                    print("You got it right! ")
                    break
                if guess > 10:
                    print(f"Your guess is not within the specified range! You have {chances} chance(s) left. ")
                else:
                    print(f"That was wrong! You have {chances} chance(s) left. ")
            else:
                if guess_count >= guess_limit:
                    print("Game Over!")
        elif level_selection == 2:
            guess_count = 0
            guess_limit = 4
            while guess_count < guess_limit:
                user_input = input("\nGuess a number between 1 and 20: ")
                guess_count += 1
                chances = guess_limit - guess_count
                try:
                    guess = int(user_input)
                except ValueError:
                    print(f"Error! Please enter only numbers. You have {chances} chance(s) left. ")
                    continue
                if guess == hidden_medium:
                    print("You got it right! ")
                    break
                if guess > 20:
                    print(f"Your guess is not within the specified range! You have {chances} chance(s) left. ")
                else:
                    print(f"That was wrong! You have {chances} chance(s) left. ")
            else:
                if guess_count >= guess_limit:
                    print("Game Over!")
        elif level_selection == 3:
            guess_count = 0
            guess_limit = 3
            while guess_count < guess_limit:
                user_input = input("\nGuess a number between 1 and 50: ")
                guess_count += 1
                chances = guess_limit - guess_count
                try:
                    guess = int(user_input)
                except ValueError:
                    print(f"Error! Please enter only numbers. You have {chances} chance(s) left. ")
                    continue
                if guess == hidden_hard:
                    print("You got it right! ")
                    break
                if guess > 50:
                    print(f"Your guess is not within the specified range! You have {chances} chance(s) left. ")
                else:
                    print(f"That was wrong! You have {chances} chance(s) left. ")
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
                print("Bye! ")
                play_again = not True
                start_game = not True


random_guess_game()
