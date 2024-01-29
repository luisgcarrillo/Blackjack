############ blackjack.py ##############
#
# Name : Luis Carrillo
#
#
# Algorithm :
# - Initialize variables for dollars, a count of rounds played, as well as lists for the deck and both player's hands 
# - Assign each card in the deck a number and suit as a 2D array
# - Shuffle the deck, keeping the numbers and suits associated but switching the order of cards in the deck
# - define drawToHand function which adds card to either player's 'hand' list when called
# - define calcScore function which takes card's number value and adds to player's hand score when called
# - define drawCard function which concatenates strings in order to display cards in a graphical manner
# - define drawDealer function which draws two cards for the dealer, displays one and hides the other
# - define postGameScreen function which displays the player's initials, dollars amd rounds played after the game
# - begin while loop that functions as the actual game, with the ability to hit or stand and win conditions
########################################

import random

playRound = "Y"
dollars = 500
roundCount = 1

deck = []

playerHand = []

dealerHand = []

deckSpot = 0

for i in range(2,15):
    deck.append([i,"<3 "]) ## hearts
for i in range(2,15):
    deck.append([i,"-C>"]) ## spades
for i in range(2,15):
    deck.append([i,"c8="]) ## clubs
for i in range(2,15):
    deck.append([i,"<> "]) ## diamonds

random.shuffle(deck)

def drawToHand(hand):
    global deckSpot
    hand.append(deck[deckSpot])
    deckSpot += 1


def calcScore(hand):

    aceCount = 0
    playerScore = 0
    
    for i in range(len(hand)): 
        if hand[i][0] <= 10:
            playerScore = playerScore + hand[i][0]
        elif hand[i][0] <= 13:
            playerScore += 10
        else:
            playerScore += 11
            aceCount += 1
        
    while aceCount > 0 and playerScore > 21: ##changes aces from 11 to 1 when in danger of busting
        playerScore -= 10
        aceCount -= 1

    return playerScore

def drawCard(hand): ## display cards by concatenating strings in order to have them appear horizontally
    cardTop = ""
    card1 = ""
    card2 = ""
    card3 = ""
    card4 = ""
    card5 = ""
    cardBot = ""
    for i in range(len(hand)): 
        suit = hand[i][1]
        numFace = hand[i][0]
        if numFace == 11:
            numFace = "J"
        elif numFace == 12:
            numFace = "Q"
        elif numFace == 13:
            numFace = "K"
        elif numFace == 14:
            numFace = "A"
        cardTop += ("|||||||||    ")
        card1 += ("|    %s|    "%(suit))
        card2 +=("|       |    ")
        card3 +=("|   %s  |    "%('{:2}'.format(numFace)))
        card4 +=("|       |    ")
        card5 +=("|%s    |    "%(suit))
        cardBot +=("|||||||||    ")
    print(cardTop)
    print(card1)
    print(card2)
    print(card3)
    print(card4)
    print(card5)
    print(cardBot)

def screen():
    print("---------------------------------------------------------------------------------")


def drawDealer(): ## display dealer's cards
        suit = dealerHand[0][1]
        numFace = dealerHand[0][0]
        if numFace == 11:
            numFace = "J"
        elif numFace == 12:
            numFace = "Q"
        elif numFace == 13:
            numFace = "K"
        elif numFace == 14:
            numFace = "A"
        print("|||||||||    |||||||||") ## Hides one of the dealers cards
        print("|    %s|    |||||||||"%(suit))
        print("|       |    |||||||||")
        print("|   %s  |    |||||||||"%('{:2}'.format(numFace)))
        print("|       |    |||||||||")
        print("|%s    |    |||||||||"%(suit))
        print("|||||||||    |||||||||")
        print("                       ")



def postgameScreen():
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print("|     PLAYER        PROFIT        ROUNDS    |")
    print("|     ------        ------        ------    |")
    print("|      %s        $%s         %s       |"%(initials,'{:7}'.format(profit),'{:2}'.format(roundCount)))
    print("|                                           |")
    print("|                                           |")
    print("|           THANK YOU FOR PLAYING!          |")
    print("|||||||||||||||||||||||||||||||||||||||||||||")




while playRound == "Y" or playRound == 'y': ## game begins
    print("Let's play Blackjack!\nYou have", dollars,"dollars to play with.")
    wager = int(input("How many dollars would you like to wager?\nMinimum Wager : $25\n"))
    while wager > dollars:
        print("You do not have enough dollars to wager that amount.")
        wager = int(input("Please enter a new wager : "))
    while wager < 25 and wager <= dollars:
        print("The minimum wager is $25. Please wager a higher amount.")
        wager = int(input("Please enter a wager higher than $25: "))
    dealerHand = []
    playerHand = []
    drawToHand(dealerHand)
    drawToHand(dealerHand)
    drawToHand(playerHand)
    drawToHand(playerHand)
    drawDealer()
    drawCard(playerHand)
    dollars = dollars - wager
    print("PLAYER SCORE:",calcScore(playerHand))
    while calcScore(playerHand) < 21:
        PlayerChoice = input("[H]it?\n[S]tand?\n")
        if PlayerChoice == "H" or PlayerChoice == "h":
             drawToHand(playerHand)
        elif PlayerChoice == "S" or PlayerChoice == "s":
            break
        else:
            print("Please enter either [H]it or [S]tand.")
            PlayerChoice = input("[H]it?\n[S]tand?\n")
        print("DEALER HAND")
        drawDealer()
        print("PLAYER HAND")
        drawCard(playerHand)
        print("PLAYER SCORE:",calcScore(playerHand))
        screen()
    ## end of game ##
    if deckSpot > 40: ## re-shuffle deck when cards are low
        random.shuffle(deck)
        deckSpot = 0
    if  calcScore(playerHand) < 21:     
        while calcScore(dealerHand) <= 16:
            drawToHand(dealerHand)
    drawCard(dealerHand) ## displays dealer's final hand
    print("DEALER SCORE :", calcScore(dealerHand))
    drawCard(playerHand) ## displays player's final hand
    print("PLAYER SCORE :", calcScore(playerHand))
    pHand = calcScore(playerHand)
    dHand = calcScore(dealerHand)
    ## win conditions
    if pHand == 21 and dHand != 21 and len(playerHand) == 2:
        print("You have a Blackjack. You win the round.\n")
        dollars = dollars + (wager * 2)
    elif dHand == 21 and pHand != 21 and len(dealerHand) == 2:			
        print("Dealer has a Blackjack. Dealer wins the round.\n")
    elif pHand == 21 and dHand == 21 and len(playerHand) == 2 and len(dealerHand) == 2:			
        print("Both you and the Dealer have a blackjack. This round is a push and your wager has been returned.\n")
        dollars = dollars + wager
    elif pHand == dHand:			
        print("Both you and the Dealer have the same hand total. This round is a push and your wager has been returned.\n")
        dollars = dollars + wager
    elif pHand > 21:
        print("Your hand is over 21. You have busted. Dealer wins the round.\n")
    elif dHand > 21:
        print("Dealer's hand is over 21. The Dealer has busted. You win the round.\n")
        dollars = dollars + (wager * 2)
    elif dHand > 21 and pHand > 21:
        print("Both you and the dealer have bust. You lose the round.")
    elif pHand < dHand:
        print("Your hand is less than the Dealer's hand. Dealer wins the round.\n")
    elif pHand > dHand:			   
        print ("Your hand is greater than the Dealer's hand. You win the round.\n")
        dollars = dollars + (wager * 2)
    print("Dollars remaining : " ,dollars)
    if dollars >= 0 and dollars <= 25 :
        print("You don't have enough money to wager and can no longer continue. Game over.\n")
        playRound = "N"
        profit = dollars - 500
        initials = input("Please enter your initials : ")
        postgameScreen()
    else:
        while playRound == "N" or playRound == "n" or playRound == "Y" or playRound == "y":
            if playRound == "N" or playRound == "n":
                initials = input("Please enter your initials : ")
                profit = dollars - 500
                postgameScreen()
                break
            else:
                playRound = input("Would you like to play another round? Enter '[Y]es' or '[N]o.'\n ")
                if playRound == "Y" or playRound == "y":
                    break
    roundCount += 1
    
    













