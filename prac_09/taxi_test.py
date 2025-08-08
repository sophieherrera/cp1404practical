from taxi import Taxi

def main():
    my_taxi = Taxi("Prius 1", 100)


    # Drive the taxi for 40km
    my_taxi.start_fare() # Start the fare
    my_taxi.drive(40)

    print(my_taxi)
    print(f"Current price: {my_taxi.get_fare():.2f}")

    # Restart meter
    my_taxi.start_fare()
    my_taxi.drive(100)

    print(my_taxi)
    print(f"Current price: {my_taxi.get_fare():.2f}")

if __name__ == "__main__":
    main()