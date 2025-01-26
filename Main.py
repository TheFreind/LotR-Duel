# Main
# While loop that contains gameflow

from Classes import *
from Functions import *
from Data import *

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


deckOfCards = setupCards(cardsRawData, "Playing Card")
deckOfLandmarks = setupCards(landmarksRawData, "Landmark")

gameEnd = False
startingPlayer = "Sauron" # Unnecessary imo

#while gameEnd == False: