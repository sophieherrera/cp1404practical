import random

MENU = """(A)Hear a compliment
(B)Add your own compliment
(C)Quit"""
compliments = [
        "You're doing amazing!",
        "You have a great sense of humor!",
        "You're doing great!",
        "Your coding skills are improving!",
    ]

print(MENU)
choice = input(">>> ").upper()   # >>> shows prompt to user, .upper() converts input into uppercase

while choice != "C":
        if choice == "A":
            print(random.choice(compliments))
        elif choice == "B":
            new_compliment = input("Enter your compliment: ")
            compliments.append(new_compliment)
            print("Compliment added")
        else:
            print("Invalid choice. try again!")

        print(MENU)
        choice = input(">>> ").upper()

print("Goodbye. :)")


