# An adventure game
from time import sleep
from random import randint
dam = 0

def typo():
    typo = randint(1, 6)
    if typo == 1:
        print("Grammar God: That isnt an option ya dum dum")
    elif typo == 2:
        print("Grammar God: Idiot, spell it right nerd")
    elif typo == 3:
        print("Grammar God: Everyone hates you for your bad spelling")
    elif typo == 4:
        print("Grammar God: LeaRn 2 spel guD")
    elif typo == 5:
        print("Grammar God: You Suck")
    

def intro():
    print("Cripples: Warrior...")
    sleep(3)
    print("Cripples: Warrior, open your eyes.")
    sleep(4)
    print("<====================================================>")
    print("Cripples: Finally, you have awoken.")
    sleep(2)
    print("Cripples: What be thy name?")
    print(" ")
    sleep(2)
    name = input("You: My name is: ")
    name = name.title()
    sleep(2)
    print(" ")
    print("Cripples: Ahh, alas", name)
    sleep(2)
    print("Cripples: Now, choose your blade, great", name)
    sleep(2)
    print("Cripples: The sword deals 4 damage however swings like the breeze")
    sleep(2)
    print("Cripples: The mace deals 7 however may not be a guaranteed hit")
    sleep(2)
    print("Cripples: The nunchucks deal 3 however may hit twice")
    sleep(2)
    print("<====================================================>")
    print("Cripples: 'SWORD' 'MACE' or 'NUNCHUCKS'")
    weapon = input("You: I choose the: ")
    weapon = weapon.upper()
    sleep(3)
    print("Good choice, great", name)
    if weapon == "sword":
        dam = 4
    elif weapon == "mace":
        dam = 7
    elif weapon == "nunchucks":
        dam = 3
    else:
        typo()
    question()
def question():
    sleep(3)
    print("Your mind: I should probable ask him a question...")
    sleep(3)
    print("<====================================================>")
    print("A: Where am I?")
    print("B: Who are you?")
    print("C: What happened to me?")
    print("<====================================================>")
    question = input("Your mind: Ill ask him: ")
    

    
    
    
    

# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    intro()
