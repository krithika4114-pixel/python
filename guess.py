import random

attempts_list = []

def show_score():

    if len(attempts_list) <= 0:
        print("there is currently no high score, it's your for the taking! ")
    else:
        print("the current high score is {} attempts".format(min(attempts_list)))



        def start_game():
            random_number = int(random.randint(1, 10))
            print("hey there! welcome to the game of guesses!")
            player_name = input("Enter your name!")
            wanna_play = input("Hi, {}, would you like to the guessing game? (enter yes/no)".format(player_name))

