from unreliable_car import UnreliableCar

def main():
    low_reliability_car = UnreliableCar("Old Bomb", 100, 20)
    high_reliability_car = UnreliableCar("Almost New", 100, 90)

    print("Testing low reliability Car:")
    for i in range(5):
        distance_driven = low_reliability_car.drive(10)
        print(f"Attempt{i + 1}: drove: {distance_driven} km, fuel left: {low_reliability_car.fuel}")

    print("\nTesting high reliability Car:")
    for i in range(5):
        distance_driven = high_reliability_car.drive(10)
        print(f"Attempt {i + 1}: drove {distance_driven} km, fuel left: {high_reliability_car.fuel}")

if __name__ == "__main__":
    main()


