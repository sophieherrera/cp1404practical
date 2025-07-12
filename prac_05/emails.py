"""
Emails
Estimate: 15 minutes
Actual: 12 minutes
"""

email_to_name = {}

email = input("Email: ")
while email != "":
    name_guess = email.split('@')[0].replace('.', ' ').title()
    confirmation = input(f"Is your name {name_guess}? (Y/n) ").strip().lower()
    if confirmation == 'n' or confirmation == 'no':
        name_guess = input("Name: ")
    email_to_name[email] = name_guess
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")

