"""Program to evaluate a user's score with a menu of options"""

def main():
    """Menu-based program to evaluate a score."""
    score = get_valid_score()

    menu = """
(G)et score
(P)rint result
(S)how stars
(Q)uit
"""
    print(menu)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_result(score))
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()

    print("Goodbye!")


def get_valid_score():
    """Prompt user for a valid score between 0 and 100."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score: "))
    return score


def determine_result(score):
    """Return result based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()