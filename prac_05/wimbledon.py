"""
Wimbledon Champions Data Processing
Estimate: 25 minutes
Actual: 15 minutes

"""

FILENAME = "wimbledon.csv"


def main():
    """Main function to orchestrate loading and displaying Wimbledon data."""
    records = load_data(FILENAME)
    champions = count_wins(records)
    countries = get_countries(records)

    print("Wimbledon Champions:")
    for name, count in champions.items():
        print(f"{name} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


def load_data(filename):
    """Load data from the Wimbledon CSV file.

    Returns a list of [year, champion, country].
    Skips the header and handles UTF-8 BOM encoding.
    """
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip header
        return [line.strip().split(",") for line in in_file]


def count_wins(records):
    """Return a dictionary of champion names and how many times each has won."""
    wins = {}
    for _, champion, _ in records:
        wins[champion] = wins.get(champion, 0) + 1
    return wins


def get_countries(records):
    """Return a sorted list of unique countries from the records."""
    return sorted({country for _, _, country in records})


if __name__ == "__main__":
    main()
