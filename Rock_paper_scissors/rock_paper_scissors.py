import random

game_options = ("rock", "paper", "scissors")

while True:
    opponent_choice = random.choice(game_options)
    val = input("Rock, Paper, Scissors? (rock/paper/scissors): ").lower()
    print(f"The opponent chose {opponent_choice}")
    if val == opponent_choice:
        print("It's a tie!")
    elif val == "rock" and opponent_choice == "scissors":
        print("You win!")
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again == "no":
            print("Thank you for playing the game, come back soon!")
            break
        elif play_again != "yes":
            print("Please enter a valid response")
            break
    elif val == "paper" and opponent_choice == "rock":
        print("You win!")
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again == "no":
            print("Thank you for playing the game, come back soon!")
            break
        elif play_again != "yes":
            print("Please enter a valid response")
            break
    elif val == "scissors" and opponent_choice == "paper":
        print("You win!")
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again == "no":
            print("Thank you for playing the game, come back soon!")
            break
        elif play_again != "yes":
            print("Please enter a valid response")
            break
    else:
        print("You lose!")
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again == "no":
            print("Thank you for playing the game, come back soon!")
            break
        elif play_again != "yes":
            print("Please enter a valid response")
            break


    