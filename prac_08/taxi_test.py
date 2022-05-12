from taxi import Taxi


def main():
    
    text_taxi = Taxi("Prius 1", 100)
    text_taxi.drive(40)
    print(text_taxi)
    text_taxi.start_fare()
    text_taxi.drive(100)
    print(text_taxi)
    
if __name__ == '__main__':
    main()