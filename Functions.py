# Functions

from Classes import *

# Setup Function
# Convert Data.py card information into Card class
# Do I move this function into Main? Probably

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





#AddPiece(Who adds? What is added?)
#RemovePiece(Who's removed? What is removed?)
#Mobilize()
#Conflict(Region)


#CheckVictory() after every turn

