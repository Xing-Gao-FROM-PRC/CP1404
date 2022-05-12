from unreliable_car import UnreliableCar


def main():
    car1 = UnreliableCar("Xing's car", 100, 90)
    car2 = UnreliableCar("Cat's car", 100, 15)

    for i in range(1, 12):
        print(f"Attempting to drive {i}km:")
        print(f"{car1.name} drove {car1.drive(i)}km")
        print(f"{car2.name} drove {car2.drive(i)}km")

    print(car1)
    print(car2)

if __name__ == '__main__':
    main()