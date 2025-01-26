# Main
# While loop that contains gameflow

from Classes import *
from Functions import *
from Data import *

def setupCards(rawData):
    CardClassList = []

    for card in rawData:
        name = card

        for detail in rawData[name]:

            if detail == "chapter":
                chapter = rawData[name][detail]

            if detail == "color":
                color = rawData[name][detail]
            
            if detail == "requirements":
                requirements = rawData[name][detail]

            if detail == "allianceSymbol":
                allianceSymbol = rawData[name][detail]

            if detail == "chainBanner":
                chainBanner = rawData[name][detail]

            ## if detail == "addSkills":
            ##     MISSING REWARDED SKILLS IN CLASS FUNCTION.

            if detail == "earnGold":
                earnGold = rawData[name][detail]

            if detail == "deploySoldiers":
                deploySoldiers = rawData[name][detail]

            if detail == "ringTravels":
                ringTravels = rawData[name][detail]

        # Create new card and append to list
        CardClassList.append( Card(name) ) 
    
    return CardClassList


deckOfCards = setupCards(cardsRawData)

gameEnd = False
startingPlayer = "Sauron" # Unnecessary imo

#while gameEnd == False: