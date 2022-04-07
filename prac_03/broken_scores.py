import random

def main():
    score = float(input("Enter score: ")) #Get the score
    print(score_level_check(score))
    print(random.randint(0,100)) #Output random score

def score_level_check(score):
    #Determine which grade the score is in
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif 50 <= score < 90:
        return "Passable"
    elif score >= 90:
        return "Excellent"


# Without user input 
def main_v2():
    score = random.randint(0,100)
    print(f"{score} is {score_level_check(score)}")

main_v2()