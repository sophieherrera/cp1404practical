from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def display_taxis(taxis):
    """Display the list of taxis with their Index."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def main():
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0

    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == "q":
            break

        elif choice == "c":
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except (ValueError, IndexError):
                print("Invalid choice.")

        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                total_bill += fare

        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")

    from prac_09.taxi import Taxi
    from prac_09.silver_service_taxi import SilverServiceTaxi

    def display_taxis(taxis):
        """Display the list of taxis with their Index."""
        print("Taxis available:")
        for i, taxi in enumerate(taxis):
            print(f"{i} - {taxi}")

    def main():
        print("Let's drive!")
        taxis = [
            Taxi("Prius", 100),
            SilverServiceTaxi("Limo", 100, 2),
            SilverServiceTaxi("Hummer", 200, 4)
        ]
        current_taxi = None
        total_bill = 0

        while True:
            print("q)uit, c)hoose taxi, d)rive")
            choice = input(">>> ").lower()

            if choice == "q":
                break

            elif choice == "c":
                display_taxis(taxis)
                try:
                    taxi_choice = int(input("Choose taxi: "))
                    current_taxi = taxis[taxi_choice]
                except (ValueError, IndexError):
                    print("Invalid choice.")

            elif choice == "d":
                if current_taxi is None:
                    print("You need to choose a taxi before you can drive")
                else:
                    current_taxi.start_fare()
                    distance = float(input("Drive how far? "))
                    current_taxi.drive(distance)
                    fare = current_taxi.get_fare()
                    print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                    total_bill += fare

            else:
                print("Invalid option")

            print(f"Bill to date: ${total_bill:.2f}")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

