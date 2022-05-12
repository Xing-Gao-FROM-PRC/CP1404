from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():

    total_payment = 0
    taxi = [Taxi("Prius", 100), 
            SilverServiceTaxi("Limo", 100, 2),
            SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    
    while menu_choice != "q":
        
        if menu_choice == "c":                                                      #Choose a taxi to drive
            
            print("Taxis available: ")
            display_taxi(taxi)
            choice_taxi = int(input("Choose taxi: "))
            
            try:
                current_taxi = taxi[choice_taxi]
            
            except IndexError:
                print("Invalid taxi choice")
        
        elif menu_choice == "d":                                                    #Drive the taxi
            
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            
            else:
                current_taxi.start_fare()
                travel_distance = float(input("Drive how far? "))
                current_taxi.drive(travel_distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_payment = total_payment + trip_cost
        
        else:                                                                       #Invalid menu choice
            print("Invalid option")
        
        print(f"Bill to date: ${total_payment:.2f}")
        print(MENU)
        menu_choice = input(">>> ").lower()
    
    out_loop(taxi,total_payment)
    

def display_taxi(taxi):                                                           #show taxi list
    for i, taxi in enumerate(taxi):
        print(f"{i} - {taxi}")

def out_loop(taxi,total_payment):
    print(f"Total trip cost: ${total_payment:.2f}")
    print("Taxis are now:")
    display_taxi(taxi)


if __name__ == '__main__':
    main()