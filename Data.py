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

# FACTION / ALLIANCE TOKENS
factionTokens = {
    "Dwarf":    ["IgnoreLandmarkCoinCost", "LandmarkRefreshTurn", "GreenMovements"],
    "Elf":      ["YellowRefreshTurn", "RedGlobalDeploy", "ElfSkillWildcard"],
    "Human":    ["YellowAdvanceRing", "RedAdditionalTroop", "DiscardDoubleValue"],
    "Hobbit":   ["HobbitEagles", "BlueGlobalOneTroop", "ChainBonusGold"],
    "Wizard":   ["WizardAdvanceRing", "WizardDeployTroops", "WizardDiscardReclaim"],
    "Ent":      ["EntRefreshTurn", "RemoveFortress", "EntRemoveSabotageMovement"]
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

### // CHAPTER 1 // ###
    "Gimli" : {
        "chapter" : 1,
        "color" : "Green",
        "requirements" : [0, 0, 0, 0, 1, 0],
        "allianceSymbol" : "Dwarf",
        "chainBanner" : "Dwarven Craftsmanship",
    }, 
    "Frodo and Sam" : {
        "chapter" : 1,
        "color" : "Green",
        "requirements" : [0, 0, 0, 0, 1, 0],
        "allianceSymbol" : "Hobbit",
        "chainBanner" : "Second Breakfast",
    }, 
    "Aragorn, son of Arathorn" : {
        "chapter" : 1,
        "color" : "Green",
        "requirements" : [0, 0, 0, 0, 0, 1],
        "allianceSymbol" : "Human",
        "chainBanner" : "Shadowfax",
    }, 
    "Legolas" : {
        "chapter" : 1,
        "color" : "Green",
        "requirements" : [0, 0, 0, 0, 0, 1],
        "allianceSymbol" : "Elf",
        "chainBanner" : "Elven Grace",
    }, 
    "Naz'gul" : {
        "chapter" : 1,
        "color" : "Gray",
        "addSkills" : {
            "Ruse" : 1
        }
    },
    "Furtive Halflings" : {
        "chapter" : 1,
        "color" : "Gray",
        "addSkills" : {
            "Ruse" : 1
        }
    },
    "Travel the Marsh" : {
        "chapter" : 1,
        "color" : "Gray",
        "addSkills" : {
            "Courage" : 1
        }
    },
    "Travel through Moria" : {
        "chapter" : 1,
        "color" : "Gray",
        "addSkills" : {
            "Courage" : 1
        }
    },
    "Forge Weapons" : {
        "chapter" : 1,
        "color" : "Gray",
        "addSkills" : {
            "Strength" : 1
        }
    },
    "Prepare Aramaments" : {
        "chapter" : 1,
        "color" : "Gray",
        "addSkills" : {
            "Strength" : 1
        }
    },
    "Claim Birthright" : {
        "chapter" : 1,
        "color" : "Gray",
        "addSkills" : {
            "Leadership" : 1
        }
    },
    "History of Middle-Earth" : {
        "chapter" : 1,
        "color" : "Gray",
        "addSkills" : {
            "Knowledge" : 1
        }
    },
    "Collect Taxes" : {
        "chapter" : 1,
        "color" : "Yellow",
        "earnGold" : 2
    },
    "Exploit the Land" : {
        "chapter" : 1,
        "color" : "Yellow",
        "earnGold" : 2
    },
    "Inherit Wealth" : {
        "chapter" : 1,
        "color" : "Yellow",
        "earnGold" : 2
    },
    "Share Belongings" : {
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
    "Fight in the Mines" : {
        "chapter" : 1,
        "color" : "Red",
        "deploySoldiers" : [1, ["Lindon","Arnor"] ],
        "chainBanner" : "Andúril", # Aragorn's Sword
    },
    "Sneak Attack" : {
        "chapter" : 1,
        "color" : "Red",
        "requirements" : [0, 1, 0, 0, 0, 0],
        "deploySoldiers" : [1, ["Gondor","Rohan"] ],
        "chainBanner" : "Bow of the Galadhrim", # Legolas's bow is gifted by Galadriel
    },
    "Smeagol's Escape" : {
        "chapter" : 1,
        "color" : "Blue",
        "requirements" : [0, 0, 0, 1, 0, 0],
        "ringTravels" : 1,
        "chainBanner" : "Bill, the Pony",
    },
    "Underlying Envy" : {
        "chapter" : 1,
        "color" : "Blue",
        "ringTravels" : 1,
    },
    "Insatiable Hunger" : {
        "chapter" : 1,
        "color" : "Blue",
        "requirements" : [1, 0, 0, 0, 0, 0],
        "ringTravels" : 1,
        "chainBanner" : "Raw Fish",
    },
    "Follow the Hobitses" : {
        "chapter" : 1,
        "color" : "Blue",
        "requirements" : [0, 0, 1, 0, 0, 0],
        "ringTravels" : 1,
        "chainBanner" : "Lembas Bread",
    },

### // CHAPTER 2 // ###
    "The Dwarves Go To War" : {
        "chapter" : 2,
        "color" : "Green",
        "requirements" : [0, 0, 0, 2, 1, 0],
        "allianceSymbol" : "Dwarf",
        "chainRequirement" : "Dwarven Craftsmanship"
    },
    "Forgotten Vault" : {
        "chapter" : 2,
        "color" : "Yellow",
        "earnGold" : 3,
        "chainBanner" : "Keys to the Treasury"
    },
    "Defending Helm's Deep" : {
        "chapter" : 2,
        "color" : "Red",
        "requirements" : [0, 0, 1, 2, 0, 0],
        "chainRequirement" : "Helmet",
        "deploySoldiers" : [2, ["Lindon","Enedwaith"] ],
        "chainBanner" : "Mithril Armor", # Armor gifted to Frodo from Bilbo Baggins.
    },

### // CHAPTER 3 // ###

}
