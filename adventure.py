# An adventure game
health = 10
sanity = 10

from time import sleep
def intro():
    print ("You awake cold, lost and nevous in a dark cell with no memory of your past,")
    sleep(4)
    print (" ")
    print ("Hours pass...")
    print (" ")
    sleep(4)
    print ("Suddenly, and loud 'THUNK' is sounded throughout the mysterious outside of the door,")
    sleep(3)
    print ("The door opens, you eyes struggle to ajust to the new light,")
    sleep(3)
    print ("You can make out a mysterious figure which is slowly reaching towards you,")
    sleep(4)
    print ("The figure grabs you by your raggy shirt and throws you onto a table outside of the cell,")
    sleep(4)
    print ("He lifts a rusty, blunt instrument which you still cant make out due to your burning eyes,")
    sleep(4)
    print ("A demonic laugh shatters your ears as the man draws closer to you,")
    sleep(4)
    print ("You can make out glistening blood, smuthered around the point of the torture weapon,")
    sleep(4)
    print ("You know you are in serious trouble and this could be the end,")
    sleep(4)
    print ("Your eyes have fully adjusted to the light and you make out a middle aged man, staring at you with a bandana covering his mouth,")
    sleep(4)
    print ("You notice a large pile of salt in the corner of your eye, you may be able to reach it...")
    print (" ")
    print (" ")
    sleep(3)
    choice1()

def choice1():
    global health
    global sanity
    print ("A: Grab the salt and throw it into his eyes")
    sleep(1)
    print ("B: Roll off the table and run for it")
    sleep(1)
    print ("C: Put up a fight and attempt to punch the armed man")
    answer = input("Pick an option: ")
    answer = answer.upper()
    if answer == "A":
        sleep(1)
        print ("You decide to Reach for the salt however the vicious man stabs you in the hand mid-action, piercing through the flesh")
        health = health - 3
        sleep(4)
        print ("-3 health")
        chapter1()
    elif answer == "B":
        print ("You make a run for it, barely escaping his grasp, you spot a rusty door and attempt to escape, however it is locked.")
        sleep(3)
        print ("The man charges towards you and knocks you to the ground with a heavy punch to your face")
        health = health - 1
        sleep(1)
        print ("-1 health")








# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    intro()
