from __future__ import division
import random

"""
    In probably my first year of college,
    I implemented a monty-hall verification experiment in C
    I wanted to get good at coding, so I cleaned it up a little
    and then a little more
    and then something suprising happened
    I thought it might be fun to recreate that,
    but I know python now.
"""



"""
    Let's implement a monty hall experiment!
"""
def singleTrial():
    #all empty
    doors = [0, 0, 0]
    #hide the prize
    correctDoor = random.randint(0,2);
    doors[correctDoor] = 1
    #player chooses a door at random
    playerChoice = random.randint(0, 2);
    #host chooses a door that is not the player's and contains no prize
    hostChoice = random.randint(0,2);
    while(hostChoice == playerChoice or hostChoice == correctDoor):
        hostChoice = random.randint(0,2)
    #player decides to switch
    playerSwitch = random.randint(0,2);
    while(playerSwitch == hostChoice or playerSwitch == playerChoice):
        playerSwitch = random.randint(0,2);
    if(playerSwitch == correctDoor):
        return 1
    else:
        return 0


N = 10**5
S = 0.0
for i in range(N):
    S += singleTrial()

print "trial 1 ", S/N #0.66913 looks like it's verified!


"""
    Let's clean it up a bit...

    First thing to notice is the player doesn't need to switch
    Let's just have them keep the door they chose and
    swap the 1 and 0 at the end so we still get our .66 eh?
"""
def singleTrial2():
    #all empty
    doors = [0, 0, 0]
    #hide the prize
    correctDoor = random.randint(0,2);
    doors[correctDoor] = 1
    #player chooses a door at random
    playerChoice = random.randint(0, 2);
    #host chooses a door that is not the player's and contains no prize
    hostChoice = random.randint(0,2);
    while(hostChoice == playerChoice or hostChoice == correctDoor):
        hostChoice = random.randint(0,2)
    #we swapped the results
    #so we'll get the same 2/3
    if(playerChoice == correctDoor):
        return 0
    else:
        return 1


N = 10**5
S = 0.0
for i in range(N):
    S += singleTrial2()

print "trial 2 ", S/N #still working


"""
    We can pick the same door every time, since the location
    of the prize is still random
"""
def singleTrial3():
    doors = [0, 0, 0]
    #https://xkcd.com/221/
    playerChoice = 0;
    #hide the prize
    correctDoor = random.randint(0,2);
    doors[correctDoor] = 1
    #host chooses a door that is not the player's and contains no prize
    hostChoice = random.randint(0,2);
    while(hostChoice == playerChoice or hostChoice == correctDoor):
        hostChoice = random.randint(0,2)
    #we swapped the results
    #so we'll get the same 2/3
    if(playerChoice == correctDoor):
        return 0
    else:
        return 1

N = 10**5
S = 0.0
for i in range(N):
    S += singleTrial3()

print "trial 3 ", S/N


"""
    The host doesn't have much of a choice anymore do they?
"""
def singleTrial4():
    doors = [0, 0, 0]
    #https://xkcd.com/221/
    playerChoice = 0;
    #hide the prize
    correctDoor = random.randint(0,2);
    doors[correctDoor] = 1
    #host chooses a door that is not the player's and contains no prize
    if(correctDoor == 1):
        hostChoice = 2
    elif(correctDoor == 2):
        hostChoice = 1
    else:
        pass #doesn't matter since we're sticking
    #we swapped the results
    #so we'll get the same 2/3
    if(playerChoice == correctDoor):
        return 0
    else:
        return 1

N = 10**5
S = 0.0
for i in range(N):
    S += singleTrial4()

print "trial 4 ", S/N

"""
    Player loses in the first 2 scenarios,
    loses in the 3rd
    Now we don't need to check if we chose right at the end
"""
def singleTrial5():
    doors = [0, 0, 0]
    #https://xkcd.com/221/
    playerChoice = 0;
    #hide the prize
    correctDoor = random.randint(0,2);
    doors[correctDoor] = 1
    #host chooses a door that is not the player's and contains no prize
    if(correctDoor == 1):
        hostChoice = 2
        return 1
    elif(correctDoor == 2):
        hostChoice = 1
        return 1
    else:
        return 0

N = 10**5
S = 0.0
for i in range(N):
    S += singleTrial5()

print "trial 5 ", S/N


"""
    In fact, who cares what the host chose?
"""
def singleTrial6():
    doors = [0, 0, 0]
    #https://xkcd.com/221/
    playerChoice = 0;
    #hide the prize
    correctDoor = random.randint(0,2);
    doors[correctDoor] = 1
    #host chooses a door that is not the player's and contains no prize
    if(correctDoor == 1):
        return 1
    elif(correctDoor == 2):
        return 1
    else:
        return 0

N = 10**5
S = 0.0
for i in range(N):
    S += singleTrial6()

print "trial 6 ", S/N


"""
    What was doors = [0, 0, 0] for again?
"""
def singleTrial7():
    #https://xkcd.com/221/
    playerChoice = 0;
    #hide the prize
    correctDoor = random.randint(0,2);
    #host chooses a door that is not the player's and contains no prize
    if(correctDoor == 1):
        return 1
    elif(correctDoor == 2):
        return 1
    else:
        return 0

N = 10**5
S = 0.0
for i in range(N):
    S += singleTrial7()

print "trial 7 ", S/N



"""
    Let's clean up the if else
"""
def singleTrial8():
    #https://xkcd.com/221/
    playerChoice = 0;
    #hide the prize
    correctDoor = random.randint(0,2);
    #
    if(correctDoor == 1 or correctDoor == 2):
        return 1
    else:
        return 0

N = 10**5
S = 0.0
for i in range(N):
    S += singleTrial8()

print "trial 8 ", S/N



"""
    The players choice doesn't matter?
    Uh...
"""
def singleTrial9():
    correctDoor = random.randint(0,2);
    if(correctDoor == 1 or correctDoor == 2):
        return 1
    else:
        return 0

N = 10**5
S = 0.0
for i in range(N):
    S += singleTrial9()

print "trial 9 ", S/N



"""
    The monty hall problem
"""
def singleTrial10():
    return int(random.randint(0,2) != 0);

N = 10**5
S = 0.0
for i in range(N):
    S += singleTrial10()

print "trial 10 ", S/N

