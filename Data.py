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
# Landmarks is meant to be a child of the Cards class.
landmarksRawData = {
    "Gray Havens" : {
        "Fortress" : "Lindon",
        "requirements" : [0, 0, 0, 3, 2, 1],
        "specialAbility" : "GrayHavenTakeAllianceTokens",
    },
    "Bree" : {
        "Fortress" : "Arnor",
        "requirements" : [0, 0, 2, 3, 1, 0],
        "deploySoldiers" : [2, ["Arnor"] ],
        "Movements" : 2
    },
    "Erebor" : {
        "Fortress" : "Rhovanion",
        "requirements" : [0, 1, 1, 2, 1, 1],
        "earnGold" : 5,
        "Movements" : 1
    },
    "Isengard" : {
        "Fortress" : "Enedwaith",
        "requirements" : [0, 2, 3, 0, 0, 1],
        "specialAbility" : "IsengardDiscardSkillCard",
        "ringTravels" : 1,
    },
    "Helm's Deep" : {
        "Fortress" : "Rohan",
        "requirements" : [0, 3, 0, 0, 2, 1],
        "deploySoldiers" : [3, ["Rohan"] ],
    },    
    "Minas Tirith" : {
        "Fortress" : "Gondor",
        "requirements" : [0, 3, 0, 1, 0, 2],  # Figure out how to calculate gold cost. Hm. Maybe in Main on "Purchase function".
        "deploySoldiers" : [1, ["Gondor"] ],
        "ringTravels" : 2,
    },
    "Barad-Dur" : {
        "Fortress" : "Mordor",
        "requirements" : [0, 0, 3, 0, 2, 1],
        "specialAbility" : "DiscardReclaim",
    },

    # The Shire

    # GROND!!!!
}

#CARDS DIRECTORY
# Class Card's __init__ does the heavy lifting here. Assume all values 0 or empty, unless said otherwise.
# A sophisticated function in Main will scan and update attributes if there is a difference.
#   -- Requirements = [Gold, Ruse, Courage, Strength, Leadership, Knowledge]
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
        "addSkills" : {
            "Ruse" : 1
        }
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
