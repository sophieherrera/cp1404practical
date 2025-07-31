from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised Taxi with fanciness and flagfall charge. """
    flagfall = 4.50 # Class variable

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Price based on price_per_km based on fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """ Return fare with flagfall included, rounded to nearest 10cents."""
        base_fare = super().get_fare()
        return round (base_fare + self.flagfall, 1)

    def __str__(self):
        """Return string with flagfall information."""
        return f"{super().__str__()} plus flagfall of $ {self.flagfall: .2f}"



