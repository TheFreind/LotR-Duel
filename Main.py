# Main
# While loop that contains gameflow

from Functions import *
  # In Functions.py , Classes.py is imported.
  # Return it here & the setupCards function if there are problems.
from Data import *

deckOfCards = setupCards(cardsRawData, "Playing Card")
deckOfLandmarks = setupCards(landmarksRawData, "Landmark")

gameEnd = False
startingPlayer = "Sauron" # Unnecessary imo

#while gameEnd == False:

"""
    START.
    Fellowship and Sauron players choose factions, earn 3/2 gold. Units are placed already.
    Shuffle alliance tokens.
    Shuffle Landmarks, draw 3.
    Divide cards into chapters and shuffle decks individually.

    START OF CHAPTER
    Assemble card structure depending on chapter
    Draw up to 3 landmarks

    TURN
    A) Take a chapter Card
      1) Pay the cost and play the card. Benefit from bonuses.
      2) Discard the card. Earn gold == current chapter. NOT chapter of card itself.

    B) Take a Landmark Tile.
      -- Pay cost, place in your area. Immediately gain a fortress in that region and other bonuses.
    
    CheckVictory() function.
    Turn then goes to next player.

    END OF CHAPTER occurs when all cards are taken. Maintain turn order as it were.

    Make functions...
      BuyCard()
      DiscardCard()
      BuyLandmark()

      EarnGold()
      EarnSkills?
      CalculateSkillCost()
      DeploySoldiers()
      Mobilization()
        Conflict()
      MoveRingQuest()
      EarnAllianceTokens()
        Double check all alliance tokens on where to slot their bonuses.
      CheckVictory()
        Quest
        All 6 unique factions
        Units/Fortresses present in all 7 regions.
        Check Victory MUST NOT occur before Conflict is resolved! Can't "dominate" before a battle is settled.
      
"""
