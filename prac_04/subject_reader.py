"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data"


def main():
    data = load_data()
    display_subjects(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    input_file = open(FILENAME)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subjects.append(parts)
        # print(parts)  # See if that worked
        # print("----------")
    input_file.close()
    return subjects

def display_subjects(subjects):
    for code, lecturer, students in subjects:
        print(f"{code} is taught by {lecturer} and has {students} students")

main()
