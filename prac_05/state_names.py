state_name = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria",
                "TAS": "Tasmania"}

state = input("Enter short state: ").upper()
while state != "":
    if state in state_name:
        print(f"{state} is {state_name[state]}")
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()