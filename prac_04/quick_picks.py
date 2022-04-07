import random

ELEMENT_NUMBER_IN_ROW = 6
MINIMUM_NUM =1
MAXMUM_NUM = 45

def main():
    quick_picks_number = int(input("How many quick picks? "))
    while quick_picks_number<0:
        print("Invalid number")
        quick_picks_number = int(input("How many quick picks? "))
    for i in range (quick_picks_number):
        quick_pick = []
        for z in range (ELEMENT_NUMBER_IN_ROW):
            number = random.randint(MINIMUM_NUM,MAXMUM_NUM)
            while number in quick_pick:
                number = random.randint(MINIMUM_NUM,MAXMUM_NUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))
            
main()