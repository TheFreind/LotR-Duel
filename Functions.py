# Functions

from Classes import *

import random

# Setup Function
# Convert Data.py card information into Card class
# Do I move this function into Main? Probably

# Used to translate data from cards into Card classes at start of game.
#   -- Array of raw data
#   -- Which class to make? 
def setupCards(rawData, type):
    CardClassList = []

    for cardName in rawData:
        print(cardName)#
        
        if type == "Playing Card":
            createCard = Card(rawData[cardName], cardName)
        elif type == "Landmark": 
            createCard = Landmark(rawData[cardName], cardName)

        createCard.defineStats(rawData[cardName])
        CardClassList.append( createCard ) 
    
    return CardClassList

# Shuffle 
#   -- Deck/stack of things to shuffle
def shuffle(stack):
    random.shuffle(stack)

# Move cards from ORIGIN array to DESTINATION array.
def moveCards(origin, destination, amount):
    if (amount < 0) or (type(amount) is not int):     # Keep. You should never see this in game.
        print("Amount invalid. Aborting moveCards.")  # Invalid "amount" to draw.

    if amount > len(origin):  # Failsafe, just in case you draw too much.
        amount = len(origin)
        print("Amount requested exceeds what's in origin. Emptying all instead.")

    for k in range( amount ):
        destination.append( origin[0] )
        del origin[0]
        


def awaitResponse(question, playerAnswer):
    match question:
        case "Y/N":
            while (playerAnswer != "Y") and (playerAnswer != "N"):
                playerAnswer = input("Try again. [Y] or [N]?\n").upper()

        case "Choose Faction":
            while (playerAnswer != "F") and (playerAnswer != "S"):
                playerAnswer = input("Try again. [F]ellowship, or [S]auron?\n").upper()



        case _: 
            "awaitResponse found an ELSE."# Default message displayed.

    return playerAnswer




#AddPiece(Who adds? What is added?)
#RemovePiece(Who's removed? What is removed?)
#Mobilize()
#Conflict(Region)


#CheckVictory() after every turn

