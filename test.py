
import random, time
   
def main():
   
    Cards_Deck = 52
    participant_One = 0
    participant_Two = 0
    pp_One_Score = 0
    pp_Two_Score = 0
   
    deck = []
    suit = []
    totalList = []
   
    deck = ["Ace","King","Queen","Jack",2,3,4,5,6,7,8,9,10]
    suit = ["of spades","of hearts","of clubs","of diamonds"]
   
    for num in deck:
        for suitType in suit:
            totalList.append(str(num) + ' ' + suitType)
   
    #print("Welcome to war. Press any button to deal a hand.")
   
    while (Cards_Deck > 0):
           
        input()
        print("Cards are being dealt!")
        print()
        Output = dealCard(totalList, participant_One, participant_Two)
        totalList = Output[0]
        participant_One = Output[1]
        participant_Two = Output[2]
        print()
        #time.sleep(2)
        scoreTup = score(participant_One, participant_Two, pp_One_Score, pp_Two_Score)
        pp_One_Score = scoreTup[0]
        pp_Two_Score = scoreTup[1]
              
        Cards_Deck -= 2
           
        print(Cards_Deck, "cards remain in the deck.")
   
        print("Participant's One score: ", pp_One_Score)
        print("Participant's Two score: ", pp_Two_Score)
   
    #print("The game of war has ended!")
    if pp_One_Score > pp_Two_Score:
        winner = 'Participant One Wins'
    elif pp_One_Score < pp_Two_Score:
        winner = 'Participant Two Wins'
    else:
        winner = 'It was a tie'
    print(f"The final score is: {pp_One_Score} to {pp_Two_Score}, {winner}")
   
def dealCard(totalList, participant_One, participant_Two):
   
    participantOneSuit = ""
    participantTwoSuit = ""
       
    participant_One = random.choice(totalList)
   
    print("Participant one: ",participant_One, participantOneSuit)
    totalList.remove(participant_One)
 
    #time.sleep(2)
    participant_Two = random.choice(totalList)
       
    print("Participant two: ",participant_Two, participantTwoSuit)
    totalList.remove(participant_Two)
   
    return totalList, participant_One, participant_Two
   
def score(participant_One, participant_Two, pp_One_Score, pp_Two_Score):
    pp_One = 0
    pp_Two = 0
    participant_One = participant_One.split()
    participant_Two = participant_Two.split()
    try:
        int(participant_One[0])
        participant_One = int(participant_One) + 3
    except:
        if participant_One[0] == "Ace":
            pp_One = 1
        elif participant_One[0] == "King":
            ppOne = 2
        elif participant_One[0] == "Queen":
            ppOne = 3
        elif participant_One[0] == "Jack":
            ppOne =4
          
    try:
        int(participant_Two[0])
        pOne = int(participant_One) + 3
    except:
        if participant_Two[0] == "Ace":
            ppTwo = 1
        elif participant_Two[0] == "King":
            ppTwo = 2
        elif participant_Two[0] == "Queen":
            ppTwo = 3
        elif participant_Two[0] == "Jack":
            ppTwo = 4
   
    #debug
    if ppOne > ppTwo:
        print("Participant 2 wins the hand!")
        pp_Two_Score += 1
   
    elif ppOne < ppTwo:
        print("Participant 1 wins the hand!")
        pp_One_Score += 1
   
    elif ppOne == ppTwo:
        print("It's a tie!")
   
    return pp_One_Score, pp_Two_Score
   
    main()