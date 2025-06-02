"""Program to evaluate a user's score with a menu of options"""

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


def get_valid_score():
    """Prompt user for a valid score between 0 and 100."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score: "))
    return score