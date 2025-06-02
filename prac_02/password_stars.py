MIN_PASSWORD_LENGTH = 8
def main():
    """Get password and display it as asterisks."""
    password= get_password()
    print_asterisks(password)

def get_password():
    """prompt user for password until it meets minimum password length."""
    password=input("Please enter your password: ")
    while len(password) < MIN_PASSWORD_LENGTH:
        print("Password must be at least 8 characters long")
        password=input("Please enter your password: ")
    return password


def print_asterisks(password):
    """Print asterisks equal to the lenth of the password. """
    print("*" * len(password))

main()


