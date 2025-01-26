# Classes


# Class Card

# Define a Card as class. All values start as null and zero. 
#   - dataArray - all raw data pulled from Data.py. The function Card.defineStats properly clothes the card.
#   - name - my custom name from Data.py. Unlike other variables, it is inherited.
class Card():
    def __init__(self, dataArray, name): # Missing addSkills

        #Basic Info
        self.name = name
        self.color = ""
        self.chapter = 0

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
        self.skills = {
            "Ruse": 0,
            "Courage": 0,
            "Strength": 0,
            "Leadership": 0,
            "Knowledge": 0,
            "Choice": ["", "", ""] # If has multiple options for skills
        }
        # Rewarded Skills go here
        #   -- Must figure out EITHER/OR skills. Better yet - have it automatically apply for you in best way possible.
        #   -- Go through skills you already own. Then, either/or's. Lastly, Elf Bonus. 


    # Used only in __init__ to give the card data.
    # REMEMBER TO DELETE THE PRINTS LATER OK?
    def defineStats(self, dataArray):

        if "chapter" in dataArray:
            self.chapter = dataArray["chapter"]
            print("My chapter is," , self.chapter)#

        if "color" in dataArray:
            self.color = dataArray["color"]
            print("My color is," , self.color)#
        
        if "requirements" in dataArray:
            self.requirements = dataArray["requirements"]
            print("My requirements are," , self.requirements)#

        if "allianceSymbol" in dataArray:
            self.allianceSymbol = dataArray["allianceSymbol"]
            print("My alliance symbol is," , self.allianceSymbol)#

        if "chainBanner" in dataArray:
            self.chainBanner = dataArray["chainBanner"]
            print("My chain is," , self.chainBanner)#

        # Infrastructure set up. Figure out how to do choices, and do them automatically too.
        if "addSkills" in dataArray:
            for skillName in dataArray["addSkills"]: 
                #if "skillName" == "Choice":
                    #blabla
                self.skills[skillName] = dataArray["addSkills"][skillName] 
            print("My skills are," , self.skills)#

        if "earnGold" in dataArray:
            self.earnGold = dataArray["earnGold"]
            print("My gold earned is," , self.earnGold)#

        if "deploySoldiers" in dataArray:
            self.deploySoldiers = dataArray["deploySoldiers"]
            print("My soldiers are," , self.deploySoldiers)#

        if "ringTravels" in dataArray:
            self.ringTravels = dataArray["ringTravels"]
            print("My rings are," , self.ringTravels)#

        print("\n")#

    def __repr__(self):
        return "{} | {}".format(self.name, self.color)




class Landmark(Card):
    def __init__(self, dataArray, name):  #Landmark specific __init__

        self.fortressLocation = dataArray["Fortress"]           
        print("Fortress located in:" , self.fortressLocation) 
        
        self.specialAbility = ""
        if "specialAbility" in dataArray:
            self.specialAbility = dataArray["specialAbility"]

        super().__init__(dataArray, name) # Inherit all Card __init__

    def __repr__(self):
        return "{} | {}".format(self.name, self.fortressLocation)


# Name == What I think card looks like
# Color/type
# Cost = { "Gold" : 1, Ruse" : 0, "Courage" : 1 , etc.}
#    -- Be mindful of chains
# Rewards. Each reward is handed out in a seperate function.
#    -- Also important because Alliance Faction bonuses need to check individual elements.

class Player():
    def __init__(self, chosenName, faction):
        self.cardsOwned = []
        self.goldOwned = 0


        if faction == "F":
            self.faction = "Fellowship"
        elif faction == "S":
            self.faction = "Sauron"

        if chosenName:
            self.name = chosenName
        else:
            self.name = self.faction


    def earnGold(self, amount):
        self.goldOwned += amount

    def loseGold(self, amount):
        self.goldOwned -= amount
        if self.goldOwned < 0:
            self.goldOwned = 0

        


