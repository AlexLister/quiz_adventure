# An adventure game
from time import sleep
from random import randint
dam = 0
killcount = 0
health = 25
curiosity = 0
maxhealth = 20
weapon = ""
beasthp = 15 + (killcount * 3)
beastdam = 3
traincount = 0
currency = 0

def instructions():
    startg = input("Enter 'START' to play. Enter 'HELP' for instructions: ")
    startg = startg.lower()
    if startg == "start":
        sleep(2)
        intro()
    elif startg == "help":
        print("""So, The basics:
Type what the story tells you to type with no spelling mistakes otherwise you'll make the Grammar God angry.
If an option has 'A:' or 'B:' or 'C:' ect. in front of it, just type 'A', 'B' or 'C' because no one likes typing long sentances,
Its really quite simple. Also, choices MATTER, so choose wisely.""")
        sleep(3)
        instructions1()
    else:
        typo()
        print(" ")
        sleep(2)
        instructions()
def instructions1():
    instructions()

def typo():
    nope = ""
    typo1 = randint(1, 6)
    if typo1 == 1:
        nope = "Grammar God: That isnt an option ya dum dum"
    elif typo1 == 2:
        nope = "Grammar God: Idiot, spell it right nerd"
    elif typo1 == 3:
        nope = "Grammar God: Everyone hates you for your bad spelling"
    elif typo1 == 4:
        nope = "Grammar God: LeaRn 2 spel guD"
    elif typo1 == 5:
        nope = "Grammar God: You Suck"
    print(nope)

def intro():
    print("<====================================================>")
    print(" ")
    print("Let me go...")
    sleep(2)
    print(" ")
    print("...")
    sleep(2)
    print(" ")
    print("please...")
    sleep(4)
    print(" ")
    print(" ")
    print("You fool.")
    sleep(2)
    print("<====================================================>")
    print("")
    sleep(3)
    print("Ecinton: Ah, finally, you have awoken.")
    sleep(2)
    print("Ecinton: What be thy name?")
    print(" ")
    sleep(2)
    name = input("You: My name is: ")
    name = name.title()
    sleep(2)
    print(" ")
    print("Ecinton: Ahh, alas", name)
    sleep(2)
    print("Ecinton: Now, choose your blade, great", name)
    sleep(3)
    weaponchoice()
def weaponchoice():
    global name
    print("Ecinton: The sword deals 4, and swings like a breeze...  (Safe)")
    sleep(2)
    print("Ecinton: The mace deals 6, yet may not hit with ease...  (Risky)")
    sleep(2)
    print("Ecinton: The nunchucks deal only 3 yet double damage may counter the fees...  (Average)")
    sleep(3)
    print("<====================================================>")
    print("Ecinton: 'SWORD' 'MACE' or 'NUNCHUCKS'")
    weapon = input("You: I choose the: ")
    weapon = weapon.lower()
    sleep(2)
    print("Ecinton: Wise choice")
    if weapon == "sword":
        dam = 4
    elif weapon == "mace":
        dam = 6
    elif weapon == "nunchucks":
        dam = 3
    else:
        typo()
        print(" ")
        sleep(2)
        weaponchoice()
        
    sleep(2)
    print("Ecinton: Come, walk with me")
    question()
def questionA():
    question()
def question():
    global curiosity
    global name
    sleep(2)
    if curiosity >= 3:
            
        print("<====================================================>")
        print("A: Where am I?")
        print("B: Who are you?")
        print("C: What happened to me?")
        print("D: What are you talking about?")
        print("<====================================================>")
                
        question = input("Your mind: Ill ask him: ")
        question = question.lower()
        if question == "a":
            sleep(1)
            print(" ")
            print("You: Where am I?")
            sleep(1)
            print("Ecinton: We're in my tower, in the far south of Nightrock. Here, you will be safe...")
            curiosity = curiosity + 1
            sleep(2)
            questionA()
        elif question == "b":
            sleep(1)
            print(" ")
            print("You: Who are you?")
            sleep(1)
            print("Ecinton: Well I be Ecinton, a wizzard trying to do good for Nightrock. Well... trying.")
            curiosity = curiosity + 1
            sleep(2)
            questionA()
        elif question == "c":
            sleep(1)
            print(" ")
            print("You: What happened to me?")
            sleep(1)
            print("Ecinton: I found you on the fields of Dablon, donked out by one of those bloody Death-Beatles.")
            curiosity = curiosity + 1
            sleep(2)
            questionA()
        elif question == "d":
            sleep(1)
            print("Ecinton: Ahh, you have not heard...")
            sleep(2)
            print("Ecinton: For months now a man named Ratherrad has been harrassing Nightrock with evil and unnatural creations known as Lerk-Beasts")
            sleep(4)
            print("Ecinton: We dont know why, however his reign must come to an end...")
            sleep(4)
            print("Ecinton: ...And you will be the warrior to end it.")
            print(" ")
            sleep(3)
            print("""
        
                         +~~~~~~~~~~~~~+
                       =|   NIGHTROCK   |=
                         +~~~~~~~~~~~~~+    """)
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            game()
        else:
            typo()
            print(" ")
            sleep(2)
            questionA()
    print(" ")
    print("<====================================================>")
    print("A: Where am I?")
    print("B: Who are you?")
    print("C: What happened to me?")
    print("<====================================================>")
    question = input("Your mind: Ill ask him: ")
    question = question.lower()    
    if question == "a":
        sleep(1)
        print(" ")
        print("You: Where am I?")
        sleep(1)
        print("Ecinton: We're in my tower, in the far south of Nightrock. Here, you will be safe...")
        curiosity = curiosity + 1
        sleep(2)
        questionA()
    elif question == "b":
        sleep(1)
        print(" ")
        print("You: Who are you?")
        sleep(1)
        print("Ecinton: Well I be Ecinton, a wizzard trying to do good for Nightrock. Well... trying.")
        curiosity = curiosity + 1
        sleep(2)
        questionA()
    elif question == "c":
        sleep(1)
        print(" ")
        print("You: What happened to me?")
        sleep(1)
        print("Ecinton: I found you on the fields of Dablon, donked out by one of those bloody Death-Beatles.")
        curiosity = curiosity + 1
        sleep(2)
        questionA()
    else:
        typo()
        print(" ")
        sleep(2)
        questionA()
def game():
    sleep(4)
    print("Ecinton: I must leave you now.")
    sleep(2)
    print("Ecinton: I have made you a magic map for your journey")
    sleep(2)
    print("Ecinton: You will be able to fast travel to any of the locations plotted on it")
    sleep(2)
    print("Ecinton: Ratherrad's castle is far north of Nightrock, however you are not ready to fight without better armour")
    sleep(4)
    print("Ecinton: You will have to train hard and prepare")
    sleep(2)
    print("Ecinton: Im off!")
    themap()

def themap():
    sleep(2)
    print("Where would you like to go?")
    print("""


    8888888888888888888888888888888888888888888
  88_____________NIGHTROCK:_______________88
88_________________________________________88
88_______________ /__\______________________88
88_________/_\___/  ▲▲\___+[C] UP NORTH_____ 88
88________/     \_/ ▲▲▲  \___ \ \_____________ 88
88_______/        \       ▲▲ \___ \ \______/  \___ 88
88______/           \___________ | |_____/     \___88
88_________________________ / /_____________88
88________________________ / /______________88
88_____________▲_▲________| |______________88
88__________▲_▲ ▲_________| |______________88
88___________▲ ▲▲▲________\ \_____________88
88__________▲__▲____▲______\ \____________88
88_______▲___▲_▲▲__________\ \___________ 88
88_________▲▲__+[B] TRAINING_| |___________ 88
88__________________________ / /___________ 88
88_________________________/ /_____________88 
88________________________/ /______________88
88_________+[A] SHOP______/ /_______________88
88_______▊▅_▊▅________| |__________▊▅__ 88
88_____▅_▅__▊▅_▊▅___ | |______▊▅▊▅___ 88
88________▅____________/ /________▊▅ ▊▅_ 88
88__▊▅_+[D] HOME______/ /____▊▅__________ 88
88___________________ / /__________________ 88 
88__________________ / /___________________ 88
  88_________________| |___________________88
    888888888888888888888888888888888888888888
    
    """)

    whereto = input("Fast Travel to: ")
    whereto = whereto.lower()
    if whereto == "d":
          home()
    elif whereto == "a":
          shop()
    elif whereto == "c":
          upnorth()
    elif whereto == "b":
          training()
    else:
        typo()
        print(" ")
        sleep(2)
        themap()

def home():
    sleep(2)
    print("You open your smooth, rustic, wooden door...")
    sleep(2)
    print("Light your stunning scented candles...")
    sleep(2)
    print("Forget about all of life's problems...")
    sleep(2)
    print("Crack open a pack of beef jerky...")
    sleep(2)
    print("Sit back, relax...")
    sleep(2)
    for count in range(1, 7):
        print("And watch season", count, " of Medieval Family.")
    sleep(4)
    print(" ")
    print("~Health Restored~")
    sleep(2)
    health = maxhealth
    themap()

def training():
    sleep(2)
    print("You enter a dark and gloomy woods known as Dunlap Descent")
    sleep(2)
    print("Chills crawl down your spine")
    sleep(2)
    print("Glowing eyes emerge from the shadows")
    sleep(2)
    combatques = input("Engage in combat? ['YES' or 'NO']: ")
    combatques = combatques.lower()
    if combatques == "yes":
        combat1()
    elif combatques == "no":
        sleep(2)
        print("Your fears overpower your might")
        sleep(2)
        print("You will not fight this day")
        sleep(2)
        themap()
    else:
        typo()
        print(" ")
        sleep(2)
        training()
def combat1():
    sleep(1)
    print("You ready your weapon...")
    sleep(2)
    for x in randint(1, 5):
        beast = ""
        if x == 1:
            beast = "Lerk-Beetle"
        elif x == 2:
             beast = "Lerk-Worm"
        elif x == 3:
             beast = "Lerk-Spider"
        elif x == 4:
             beast = "Lerk-Snake"
    print("Out from the bushes approaches a giant, terrifying", beast)
    print("<====================================================>")
    print(" Your health is", health, ", your damage is", dam, " Your currency is", currency)
    print(" Your enemys health is", beasthp, ", their damage is", beastdam)
    print("<====================================================>")
    sleep(3)
    print(" ")
    print(" ")
    print(" ")
    combat()

def combat():
    crithit = 0
    global health
    global dam
    global beasthp
    global beastdam
    global weapon
    global beast
    sleep(2)
    print(" ")
    print(" ")
    print(" ")
    print("<====================================================>")
    print("                              YOUR TURN:")
    print("<====================================================>")
    print("[A]: Attack head (Double damage) (50% chance)")
    print("[B]: Attack body (Normal damage) (Normal chance)")
    print("[C]: Swipe feet (33% damage) (Enemy attack has a 50% chance)")
    print("[D]: Reflect (Reflects enemy damage) (Enemy hits at 50% damage) (50% chance)")
    print("[E]: Run (Flee from fight) (80% chance of escape)")
    print("<====================================================>")
    print(" ")
    answer = input("Your choice: ")
    answer = answer.lower()
    sleep(2)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    if weapon == "mace":
        for damage in randint(1, 4):
            if damage == 1:
                dam = 0
                print("-Your heavy mace was too slow and the", beast, " dodged your attack")
            else:
                dam = dam
                print("-Your mace hit at its normal damage striking a painful blow")
    elif weapon == "nunchucks":
        for nundam in randint(1, 4):
            if nundam == 1:
                dam = dam + dam
                print("-Your nunchucks came to use and hit TWICE dealing double damage!")
            else:
                dam = dam
                print("-Your nunchucks only attacked once striking an underwhelming blow")
    if answer == "a":
        for something in randint(1, 101):
            if something > 50:
                dam = 0
                print("-Your swing for the head was risky and missed")
            else:
                dam = dam + dam
                print("-Your swing was successful and you have dealt DOUBLE DAMAGE!")
    elif answer == "c":
        dam = dam / 3
        health = health + beastdam - (beastdam / 3)
        print("-You swiped the enemys feet and dealt a small amount of damage")
        for beastattack in randint(1, 101):
                if beastattack > 50:
                    beastdam = 0
                else:
                    beastdam = beastdam
    elif answer == "d":
        for chance in randint(50, 101):
            if chance > 50:
                dam = beastdam
                print("-You have successfully reflected the beasts damage")
            else:
                dam = 0
                print("-You messed up and did not reflect the attack")
    elif answer == "e":
        for chance2 in randint(1, 10):
            if chance2 < 8:
                print("You run as fast as you can, barely escaping the beasts grasp...")
                sleep(3)
                themap()
                
    else:
        typo()
        print(" ")
        sleep(3)
        combat()
        
    for chance2 in randint(1, 101):
        if chance2 > 50:
            beastdam = beastdam + beastdam
            crithit = 1

    beasthp = beasthp - dam
    health = health - beastdam
    if health < 1:
        health = 0
    if beasthp < 1:
        killcount = killcount + 1
        beasthp = 0

    print("-You attacked the", beast, " with a total damage of", dam)
    print(" ")
    continue1 = input("Press enter to continue: ")
    sleep(2)
    print(" ")
    print("<====================================================>")
    print("                            ENEMYS TURN:")
    print("<====================================================>")
    sleep(1)
    if beastdam == 0:
        print("-Due to your feet swipe the", beast, " missed his attack")
    elif crithit == 1:
        print("-The", beast, " attacked you in the head where it is critical")
    else:
        print("-The", beast, " attacked you in the body meaning you took normal damage")
    sleep(1)
    print("-The", beast, " attacked you with a total damage of", beastdam)
    sleep(1)
    print(" ")
    print(" ")
    print(" ")
    print("<====================================================>")
    print(" Your health is", health, ", your damage is", dam)
    print(" Your enemys health is", beasthp, ", their damage is", beastdam)
    print("<====================================================>")
    continue2 = input("Press enter to continue: ")
    sleep(2)
    if health == 0 and beasthp > 0:
        print("A cold wind blows past your ears,")
        sleep(3)
        print("blood seeps down your body,")
        sleep(3)
        print("Everything stops...")
        sleep(5)

        wakeup()
    elif health == 0 and beasthp == 0:
        print("You watch the beast thud to the ground.")
        sleep(3)
        print("This is the end...")
        sleep(3)
        print("But wait...")
        sleep(1)
        print("The beast...")
        sleep(1)
        print("It releases a gas...")
        sleep(1)
        print("Your wounds close up...")
        sleep(1)
        print("You lift off the grass...")
        sleep(1)
        print("You tighten your fists...")
        sleep(1)
        print("You regain your mass...")
        sleep(1)
        print("You have another chance.")
        sleep(3)
        health = 1
        print("Your health is now 1.")
        sleep(2)
        print("Go home, get some rest")
        themap()
    elif health > 0 and beasthp > 0:
        combat()
    else:
        print("You watch as your foe drops to the ground.")
        sleep(2)
        print("You find it...")
        sleep(2)
        print("Satisfying.")
        sleep(2)
        for orbs in randint(6, 13):
            print("You have recieved", orbs, " Lerk-Orbs")
            currency = currency + orbs
            sleep(2)
            fighton()
def fighton():
        fighton = input("[A] Fight on or [B] Leave the forest: ")
        fighton = fighton.lower()
        if fighton == "a":
            sleep(1)
            combat1()
        elif fighton == "b":
            sleep(1)
            themap()
        else:
            typo()
            sleep(2)
            print(" ")
            fighton()
        
        
        
        
        
        
    
    
        
    
 
    

# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
     training()
