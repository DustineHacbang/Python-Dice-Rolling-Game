# print("Hello World")
import random
while True:
    random_number = random.randint(1, 100)    
    value = int(input("guess the number between 1 and 100: "))
    while value != random_number:
        if value == random_number:
            print("You guessed the number!")
            break
        elif value < random_number:
            print ("too low! try again!")
        elif value > random_number:
            print ("too high! try again!")
        value = int(input("guess the number between 1 and 100: "))


    val_to_continue = input("Would you like to continue? (yes/no): ").lower()
    if val_to_continue == "no":
        print("Thank you for playing the game, come back soon!")
        break
    elif val_to_continue != "yes":
        print("Please enter a valid response")
        break