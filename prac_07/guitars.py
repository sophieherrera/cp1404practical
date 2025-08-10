"""
CP1404
Guitars program- store, display and work with Guitar objects

Estimated time: 20 min
Actual time: 25 min
"""

from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Guitar program- get and display guitars."""
    print("My Guitars!")

    guitars = load_guitars(FILENAME)
    print("These are the existing guitars:")
    display_guitars(guitars)

    guitars.extend(get_new_guitars())

    guitars.sort()
    print("\nSorted guitars:")
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)

def load_guitars(filename):
    """Load the guitars from a CSV file."""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def display_guitars(guitars):
    """Display the guitars."""
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

def get_new_guitars():
    """Return a list of new guitars."""
    new_guitars = []
    print("\nAdd New Guitars")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitars.append(Guitar(name, year, cost))
        print(f"{name} added.")
        name = input("Name: ")
    return new_guitars

def save_guitars(filename, guitars):
    """Save all guitars to the CSV file."""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

if __name__ == "__main__":
    main()

