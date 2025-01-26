# Main
# While loop that contains gameflow

from Functions import *
  # In Functions.py , Classes.py is imported.
  # Return it here & the setupCards function if there are problems.
from Data import *



# Setup Cards
allCardsUnfiltered = setupCards(cardsRawData, "Playing Card")
chapter1deck = []
chapter2deck = []
chapter3deck = []
pickableCards = []
discardDeck = []

for card in allCardsUnfiltered:
    if card.chapter == 1:
        moveCards(allCardsUnfiltered, chapter1deck, 1)
    elif card.chapter == 2:
        moveCards(allCardsUnfiltered, chapter2deck, 1)
    elif card.chapter == 3:
        moveCards(allCardsUnfiltered, chapter2deck, 3)

shuffle(chapter1deck)
shuffle(chapter2deck)
shuffle(chapter3deck)


# Setup Landmarks
deckOfLandmarks = setupCards(landmarksRawData, "Landmark")
shuffle(deckOfLandmarks)
pickableLandmarks = []
moveCards(deckOfLandmarks, pickableLandmarks, 3)

# Shuffle Alliance tokens
for faction in factionTokens:
    shuffle(factionTokens[faction])

gameEnd = False
startingPlayer = "Sauron" # Unnecessary imo

print("Welcome to LotR: Duel for Middle-Earth.\n Please select a faction to play as:")
solo_player_chooses = input("[F]ellowship, or [S]auron?\n").upper()
awaitResponse("Choose Faction", solo_player_chooses)

print("\nExcellent! Do you want a special name for yourself?")
solo_player_name_bool = input("'[Y], I want a name'; or '[N], just label me as the faction'?\n").upper()
awaitResponse("Y/N", solo_player_name_bool)

if solo_player_name_bool == "Y":
    solo_player_name = input("-- Please enter a name: \n")
else:
    solo_player_name = ""

solo_player = Player(solo_player_name, solo_player_chooses)


#while gameEnd == False:

"""
    START.
    Fellowship and Sauron players choose factions, earn 3/2 gold. Units are placed already.
    Shuffle alliance tokens.
    Shuffle Landmarks, draw 3.
    Divide cards into chapters and shuffle decks individually.

    START OF CHAPTER
    # Assemble card structure depending on chapter
    # Draw up to 3 landmarks
    if CHAPTER = 1:
    elif CHAPTER = 2:
    elif CHAPTER = 3:
    else:
      Game ends. Do end-of-chapter-3 scoring (it's domination based)


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
