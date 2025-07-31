"""
CP1404 Practical
Guitar Class

Estimated time: 20 min
Actual time: 18 min
"""

class Guitar:
    """Represent a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Create a new guitar instance with name, year and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar."""
        current_year = 2025
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age() >= 50