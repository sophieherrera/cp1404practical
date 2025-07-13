"""
CP1404
Guitars program- store, display and work with Guitar objects

Estimated time: 20 min
Actual time: 25 min
"""

from guitar import Guitar

def main():
    """Guitar program- get and display guitars."""
    print("My Guitars!")

    guitars = []

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar.name} added.\n")
        name = input("Name: ")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

main()

