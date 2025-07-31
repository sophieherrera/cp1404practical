from silver_service_taxi import SilverServiceTaxi

def main():
    fancy_taxi = SilverServiceTaxi("Limo", 100, 2)

    fancy_taxi.drive(18) # Test with 18km
    fare = fancy_taxi.get_fare()
    print(f"Fare should be $48.80. Actual: $ {fare:.2f}")
    assert fare == 48.80, f"Expected $48.80, but got ${fare:.2f}"

    print(fancy_taxi)

if __name__ == "__main__":
    main()
