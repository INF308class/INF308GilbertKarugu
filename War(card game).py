import random



Card_Deck = []
Card_Ranks = ["A", "2", "4", "5", "6", "7", "8", "9", "10" ,"J" ,"Q", "K"]
Card_Suits = [ "Hearts", "Spades", "Clubs","Diamonds"]

for Rank in Card_Ranks:
    for Suit in Card_Suits:
        Card_Deck.append(Rank + " of " + Suit)
        Card = random.choice(Card_Deck)
        print (Card)