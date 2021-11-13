import random
def main ():




    Card_Deck  = 52
    playerOne = 0
    playerTwo = 0
    pOneScore = 0
    pTwoScore = 0
   
    deck = []
    suit = []
    totalList = []
   
    deck = ["Ace","King","Queen","Jack",2,3,4,5,6,7,8,9,10]
    suit = ["of spades","of hearts","of clubs","of diamonds"]
   
    for num in deck:
        for suitType in suit:
            totalList.append(str(num) + ' ' + suitType)
   
    print("Press play button to deal a hand.")
       
    while (Card_Deck  > 0):
           
        input()
        print("Cards are being dealt!")
        print()
        theOutput = dealCard(totalList, playerOne, playerTwo)
        totalList = theOutput[0]
        playerOne = theOutput[1]
        playerTwo = theOutput[2]
        print()
        
        scoreTup = score(playerOne, playerTwo, pOneScore, pTwoScore)
        pOneScore = scoreTup[0]
        pTwoScore = scoreTup[1]
              
        Card_Deck  -= 2
           
        print(Card_Deck, "cards remain in the deck.")
   
        print("Player one's score: ", pOneScore)
        print("Player two's score: ", pTwoScore)
   
    print("The game has ended!")
    if pOneScore > pTwoScore:
        winner = 'Player One Wins'
    elif pOneScore < pTwoScore:
        winner = 'Player Two Wins'
    else:
        winner = 'It was a tie'
    print(f"The final score is: {pOneScore} to {pTwoScore}, {winner}")
   
def dealCard(totalList, playerOne, playerTwo):
   
    playerOneSuit = ""
    playerTwoSuit = ""
       
    playerOne = random.choice(totalList)
   
    print("Player one: ",playerOne, playerOneSuit)
    totalList.remove(playerOne)
 
    
    playerTwo = random.choice(totalList)
       
    print("Player two: ",playerTwo, playerTwoSuit)
    totalList.remove(playerTwo)
   
    return totalList, playerOne, playerTwo
   
def score(playerOne, playerTwo, pOneScore, pTwoScore):
    pOne = 0
    pTwo = 0
    playerOne = playerOne.split()
    playerTwo = playerTwo.split()
    try:
        int(playerOne[0])
        pOne = int(playerOne) + 3
    except:
        if playerOne[0] == "Ace":
            pOne = 1
        elif playerOne[0] == "King":
            pOne = 2
        elif playerOne[0] == "Queen":
            pOne = 3
        elif playerOne[0] == "Jack":
            pOne =4
          
    try:
        int(playerTwo[0])
        pOne = int(playerOne) + 3
    except:
        if playerTwo[0] == "Ace":
            pTwo = 1
        elif playerTwo[0] == "King":
            pTwo = 2
        elif playerTwo[0] == "Queen":
            pTwo = 3
        elif playerTwo[0] == "Jack":
            pTwo = 4
   
   
    if pOne > pTwo:
        print("Player 2 wins the hand")
        pTwoScore += 1
   
    elif pOne < pTwo:
        print("Player 1 wins the hand")
        pOneScore += 1
   
    elif pOne == pTwo:
        print("It's a tie")
   
    return pOneScore, pTwoScore
main ()  