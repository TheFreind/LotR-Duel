# Library of information

# Name : [  [# Fellowship Soldiers, # Sauron Soldiers],
#           [# Fellowship Fortress, # Sauron Fortress],
#           [Adjacent Regions] ];
regions = {
    "Lindon":   [ [0,0] , [0,0], ["Arnor"] ],
    "Arnor":    [ [2,0] , [0,0], ["Lindon", "Enedwaith", "Rhovanion"] ],
    "Rhovanion":[ [0,0] , [0,0], ["Arnor", "Enedwaith", "Rohan"] ],
    "Enedwaith":[ [0,0] , [0,0], ["Arnor", "Gondor", "Rohan", "Rhovanion"] ],
    "Rohan":    [ [0,0] , [0,0], ["Enedwaith", "Gondor", "Mordor", "Rhovanion"] ],
    "Gondor":   [ [0,0] , [0,0], ["Rohan", "Enedwaith", "Mordor"] ],
    "Mordor":   [ [0,2] , [0,0], ["Rohan", "Gondor"] ]
}

# 15 Circles, starting on circle 1, needing 14 steps to win.
# Track progress of each player.
# Track if bonuses (gold, soldiers, etc) for [Fellowship] and [Sauron] have been earned
oneRingQuest = {
    "Fellowship" : 0,
    "Sauron" : 0,
    "Bonuses" : [ [False,False,False,False] , [False,False,False,False] ]
}


#LANDMARKS DIRECTORY

#CARDS DIRECTORY
# Class Card's __init__ does the heavy lifting here. Assume all values 0 or empty, unless said otherwise.
# A sophisticated function in Main will scan and update attributes if there is a difference.
cardsRawData = {
    "Gimli" : {
        "chapter" : 1,
        "color" : "Green",
        "requirements" : [0, 0, 0, 0, 1, 0],
        "allianceSymbol" : "Dwarf",
        "chainBanner" : "Anvil",
    }, 
    "Naz'gul" : {
        "chapter" : 1,
        "color" : "Gray",
        "addSkills" : ["Ruse", 1]
    },
    "Riches" : {
        "chapter" : 1,
        "color" : "Yellow",
        "earnGold" : 2
    },
    "Gondor Warband" : {
        "chapter" : 1,
        "color" : "Red",
        "deploySoldiers" : [1, ["Enedwaith","Rhovanion"] ],
        "chainBanner" : "Helmet",
    },
    "Smeagol's Escape" : {
        "chapter" : 1,
        "color" : "Blue",
        "requirements" : [0, 0, 1, 0, 0, 0],
        "ringTravels" : 1,
        "chainBanner" : "Horse",
    },
}

# DEBUGGING. TEST IF LIST IS WORKING
#print(cardsRawData)
#for cardName in cardsRawData:
#    print(cardName)
#    print("Effects: ", cardsRawData[cardName])
