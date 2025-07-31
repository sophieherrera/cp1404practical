class Band:
    """Band has Musicians(association)."""

    def __init__(self, name):
        """Initialise a Band with a namee and empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician."""
        self.musicians.append(musician)

    def play(self):
        """Play the band."""
        for musician in self.musicians:
            print(musician.play())

    def __str__(self):
        """Return a string representation of the band."""
        return f"{self.name} ({', '.join(str(m) for m in self.musicians)})"
