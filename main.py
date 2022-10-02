from random import randint
from time import sleep
def ai():
    choices = ["rock", "paper", "scissors"]
    ai_choice = randint(0, 2)
    return choices[ai_choice]


def compare(uChoice, aChoice):
    if uChoice == aChoice:
        return "Tie!"

    map1 = ['rock', 'paper', 'scissors'] 
    map2 = ['scissors', 'rock', 'paper']

    a_beats_b = zip(map1, map2)
    for u, a in a_beats_b:
        if uChoice == u:
            if aChoice != a:
                return "You Lost!"
            else:
                return "You Won!"



def main():
    print("Welcome to Rock Paper Scissors")
    print("Pick a choice")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    user_choice = None
    ai_choice = ai()
    match int(input()):
        case 1:
            user_choice = "rock"
            print("You chose rock!")
        case 2:
            user_choice = "paper"
            print("You chose paper!")
        case 3:
            user_choice = "scissors"
            print("You chose scissors!")
        case _:
            print("Not a valid choice")
            print("Please try again \n")
    print("Rock!")
    sleep(1)
    print("Paper!")
    sleep(1)
    print("Scissors!")
    sleep(1)
    print("\n")
    print(f"The ai chose {ai_choice.title()}!")
    print(compare(user_choice, ai_choice))


if __name__ == "__main__":
    main()
