#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
import art
print (art.number_game_logo)

#Generate a random number
random_number = random.randint(0,101)
print(f"PS. The random number = {random_number}")

#Welcome message
print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100. Can you guess what it is?")
difficulty_level = input("Choose a difficulty: 'easy' or 'hard'\n").lower()

#Set number of lives. "5" for easy level and "10" for hard level.
lives = [5,10]

if difficulty_level == "easy":
    number_of_lives = lives[1]
else:
    number_of_lives = lives[0]
print(number_of_lives)


game_over = False

while not game_over:
    user_guess = int(input("What is your guess?\n"))
    if user_guess == random_number:
        print("That's correct!")
        game_over = True
    else:
        number_of_lives -=1
        if number_of_lives == 0:
            game_over = True
            print(f"Sorry, you ran out of attempts! The correct answer is {random_number}.")
        elif user_guess < random_number:
            print(f"That's too low, guess again. You have {number_of_lives} attempts left. ")
        else:
            print(f"That's too high, guess again. You have {number_of_lives} attempts left.")
        
