# Functions

# Setup Function
# Convert Data.py card information into Card class
# Do I move this function into Main? Probably
def setupForgeCards(rawData):
    for card in rawData:
        name = card
        print(name)#
        for detail in rawData[name]:

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

        return Card(name) 



#AddPiece(Who adds? What is added?)
#RemovePiece(Who's removed? What is removed?)
#Mobilize()
#Conflict(Region)


#CheckVictory() after every turn

