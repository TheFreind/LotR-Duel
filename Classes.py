# Classes


# Class Card

class Card():
    def __init__(self, name, color, chapter, chainRequirement, requirements,
                 chainBanner, allianceSymbol, earnGold, deploySoldiers, ringTravels): # Missing addSkills
        # I need to figure out how to make parameters optional to begin with.


        #Basic Info
        self.name = name
        self.color = "" # CANNOT BE EMPTY
        self.chapter = ""

        #Costs 
        self.chainRequirement = ""
        self.requirements = {
            "Gold": 0,
            "Ruse": 0,
            "Courage": 0,
            "Strength": 0,
            "Leadership": 0,
            "Knowledge": 0
        }

        #Benefits
        self.chainBanner = ""
        self.allianceSymbol = ""
        self.earnGold = 0
        self.deploySoldiers = ""
        self.ringTravels = 0
        # Rewarded Skills go here
        #   -- Must figure out EITHER/OR skills. Better yet - have it automatically apply for you in best way possible.
        #   -- Go through skills you already own. Then, either/or's. Lastly, Elf Bonus. 

        # DEBUGGING
        print("Created the", self.name, "card!")






# Name == What I think card looks like
# Color/type
# Cost = { "Gold" : 1, Ruse" : 0, "Courage" : 1 , etc.}
#    -- Be mindful of chains
# Rewards. Each reward is handed out in a seperate function.
#    -- Also important because Alliance Faction bonuses need to check individual elements.


# Class Landmark