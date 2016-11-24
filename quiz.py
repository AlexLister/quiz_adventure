# Our quiz!

from time import sleep
respect = 0
name = ""

def quiz():
    global name
    
    print ("what be thy name")

    name = ""
    for n in range(5):
        name = input("choose name: ")
        name = name.title()
        if name == "Gandalf":
            print ("YOU AINT MAGIC YOU LIAR, THERES ONLY 1 GANDALF")
            if n == 4:
                print("ENOUGH OF YOUR LIES!")
                quit()
        else:
            break

    print ("what is up Comic Sans master " + name + ", im your host, computer source code")
    print ("lets get right, INTO THE QUIZ")
    sleep(2)
    print (" ")
    Question1()

    
def Question1():
    global respect
    print ("Question 1:")
    sleep(1)
    print ("Is comic sans the best font in all of existance ever?")
    sleep(1)
    answer = input("Yarp Or Narp?: ")
    answer = answer.lower()
    if answer == "yarp":
        respect = respect + 100
        print(" + 100 respect for you sir, you damn fine being")
    elif answer == "narp":
        respect = respect - 50
        print("You have just discusted gandalf and gave Donald Trump crippling depression")
    elif answer == "Lets talk about that...":
        print("You win all the respects")
        respect = respect + 1000
    else:
        print("lern 2 spel nerd")
        sleep(3)
        Question1()
    Question2()

def Question2():
    global name
    global respect
    print ("Question 2:")
    sleep(1)
    print ("Potatoes aint just for eatin'")
    sleep(1)
    answer2 = input("True or false: ")
    answer2 = answer2.lower()
    if answer2 == "true":
        print("You have shown great promise " + name)
        respect = respect + 100
    elif answer2 == "false":
        print("you have disappointed Holy Lord Master Gandalf")
        respect = respect - 50
    elif answer == "Lets talk about that...":
        print("You win all the respects")
        respect = respect + 1000
    else:
        print("lern 2 spel nerd")
        sleep(3)
        Question2()
    Question3()

def Question3():
    global respect
    print("Question2:")
    sleep(1)
    print("Can The Majesctic Awesome Handsome Alex be bothered to make any more questions?")
    sleep(1)
    answer3 = input("Nope or Nope: ")
    answer3 = answer3.lower()
    if answer3 == "nope":
        print("yup, you win")
        respect = respect + 100
        sleep(1)
        print("Now get the hell out of my game")
        print("Respect =", respect)
        sleep(4)
        quit()
    elif answer == "Lets talk about that...":
        print("You have abused a mighty power", name)
        respect = respect - 100000000
        print("respect =", respect)
    
    else:
        print("You will suffer a bloody fate ", name)
        sleep(1)
        print("respect = -666")
        sleep(4)
        quit()
        
        
        
    
    





# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
