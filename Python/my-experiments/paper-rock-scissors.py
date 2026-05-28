import random


def my_game():
    options = ["paper", "rock", "scissors"]
    print("Options: ", options)

    human_choice = input("Choose an option: ").lower()
    computer_choice = random.choice(options)

    print("Human: ", human_choice)
    print("Computer: ", computer_choice)

    if human_choice not in options:
        print("Your option is not valid")
    elif human_choice == computer_choice:
        print("Draw")
    elif (
        human_choice == "paper"
        and computer_choice == "rock"
        or human_choice == "rock"
        and computer_choice == "scissors"
        or human_choice == "scissors"
        and computer_choice == "paper"
    ):
        print("You win")
    else:
        print("You lose")


while True:
    print("**********************")
    print("1. Start game")
    print("2. Exit")
    print("**********************")
    print("Write an option")

    option = input()

    if option == "1":
        my_game()
    elif option == "2":
        print("Exiting...")
        break
    else:
        print("Write 2 to exit")

print("End of the program")
