suits = ("Clubs", "Diamonds", "Hearts", "Spades")
picturecards = ("Jack", "Queen", "King")
value = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
playerhand = []
dealerhand = []
playervalue = []
dealervalue = []
import random
import time

def shuffler(counter, playerhit):
    playerchosensuit = (suits[random.randrange(4)])
    playerchosenvalue = (value[random.randrange(10)])
    
    if playerchosenvalue == 1:
        playerchosenvaluestr = "Ace"
        validinput = 0
        while validinput == 0:
            playerchosenvalue = input("Would you like your Ace to be worth 1 or 11?: ")
            if playerchosenvalue == "11":
                playerchosenvalue = 11
                validinput = 1
            elif playerchosenvalue == "1":
                playerchosenvalue = 1
                validinput = 1
            else:
                validinput = 0
                print("------------------------------")
                print("ERROR: Please enter either 1 or 11")
                print("------------------------------")
    elif playerchosenvalue == 10:
        playerchosenvaluestr = (picturecards[random.randrange(3)])
    else:
        playerchosenvaluestr = playerchosenvalue
    playervalue.append(playerchosenvalue)
    
    try:
        playerhand.append((playerchosenvaluestr) + " of " + playerchosensuit)
    except:
        playerhand.append(str(playerchosenvalue) + " of " + playerchosensuit)
    outputs(counter, playerhit)

def hitstand(counter, playerhit):
    playerhit = playerhit + 1 
    time.sleep(3)
    choice = input("Hit or Stand?: ")
    print("------------------------------")
    if choice == "Hit" or choice == "hit":
        shuffler(counter, playerhit)
    elif choice == "Stand" or choice == "stand":
        outputs(counter, playerhit)
    elif choice != "Hit" or choice != "hit" or choice != "Stand" or choice != "stand":
        print("ERROR: Invalid Entry")
        print("------------------------------")
        hitstand(counter, playerhit)

def dealerinit(dealercounter, counter, playerhit):
    dealerchosensuit = (suits[random.randrange(4)])
    dealerchosenvalue = (value[random.randrange(10)])
    
    if dealerchosenvalue == 1:
        dealerchosenvaluestr = "Ace"
        validinput = 0
        while validinput == 0:
            acevalue = (1, 11)
            dealerchosenvalue = str(acevalue[random.randrange(2)])
            if dealerchosenvalue == "11":
                dealerchosenvalue = 11
                validinput = 1
            elif dealerchosenvalue == "1":
                dealerchosenvalue = 1
                validinput = 1
            else:
                validinput = 0
                print("------------------------------")
                print("ERROR: Please enter either 1 or 11")
                print("------------------------------")
    elif dealerchosenvalue == 10:
        dealerchosenvaluestr = (picturecards[random.randrange(3)])
    else:
        dealerchosenvaluestr = dealerchosenvalue
    dealervalue.append(dealerchosenvalue)
    
    try:
        dealerhand.append((dealerchosenvaluestr) + " of " + dealerchosensuit)
    except:
        dealerhand.append(str(dealerchosenvalue) + " of " + dealerchosensuit)
    dealeroutputs(dealercounter, counter, playerhit)

def dealerhitstand(dealercounter, playerhit, counter):
    playerhit = playerhit + 1
    if sum(dealervalue) >= 17:
        print("Dealer Stands!")
        print("------------------------------")
        outputs(playerhit, counter)
    elif sum(dealervalue) < 17:
        print("Dealer Hits!")
        print("------------------------------")
        dealerinit(dealercounter, counter, playerhit)

def master():
    global playerhit
    counter = 0
    playerhit = 0
    outputs(counter, playerhit)
def dealermaster():
    global dealercounter
    global dealerhit
    counter = 0
    dealercounter = 0
    dealerhit = 0
    playerhit = 0
    dealeroutputs(dealercounter, counter, playerhit)

def dealeroutputs(dealercounter, counter, playerhit):
    if dealercounter < 2:
        dealercounter = dealercounter + 1
        dealerinit(dealercounter, counter, playerhit)
    elif dealercounter >= 2:
        if sum(dealervalue) > 21:
            time.sleep(3)
            print("Dealer has:", (", ".join(dealerhand)))
            print("The value of the dealer's current hand is: " + str(sum(dealervalue)))
            print("------------------------------")
            print("YOU WIN!")
            print("------------------------------")
        elif sum(dealervalue) == 21:
            time.sleep(3)
            print("Dealer has:", (", ".join(dealerhand)))
            print("The value the dealer's current hand is: " + str(sum(dealervalue)))
            print("------------------------------")
            print("YOU LOSE!")
            print("------------------------------")
        else:
            time.sleep(3)
            print("Dealer has:", (", ".join(dealerhand)))
            print("The value of the dealer's current hand is: " + str(sum(dealervalue)))
            outputs(counter, playerhit)

def outputs(counter, playerhit):
    if counter < 2:
        counter = counter + 1
        shuffler(counter, playerhit)
    elif counter >= 2:
        if sum(playervalue) > 21:
            time.sleep(3)
            print("You have:", (", ".join(playerhand)))
            print("The value of your current hand is: " + str(sum(playervalue)))
            print("------------------------------")
            print("YOU LOSE!")
            print("------------------------------")
        elif sum(playervalue) == 21:
            time.sleep(3)
            print("You have:", (", ".join(playerhand)))
            print("The value of your current hand is: " + str(sum(playervalue)))
            print("------------------------------")
            print("YOU WIN!")
            print("------------------------------")
        else:
            time.sleep(3)
            print("------------------------------")
            print("You have:", (", ".join(playerhand)))
            print("The value of your current hand is: " + str(sum(playervalue)))
            if (playerhit % 2) == 0:
                print(playerhit)
                print(1)
                hitstand(counter, playerhit)
            else:
                print(2)
                dealerhitstand(dealercounter, playerhit, counter)

dealermaster()