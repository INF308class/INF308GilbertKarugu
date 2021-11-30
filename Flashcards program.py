import random

def action():
    global Flashcards
    Flashcards ={}
    while True:
        answer = input("Select from the Menu \n"
                       "1.) Add new Flashcard question\n"
                       "2.) List answer for Flashcard\n"
                       "3.) Correct Answer\n"
                       "4.) Incorrect answer\n"
                       "Q.) Quit\n\n")
                      
    
                       
         
        if answer == "1" :
            print(Flashcards.values())
        elif answer == "2":           
            Question = str(input("\nWhat is the question ?  \n"))
            correct = str(input("\nWhat is the right answer  \n"))
            #method = str(input('\nHow is the meal prepared  \n'))
            Flashcards[Question] = [Question,correct]
            print(Flashcards[Question])
         elif answer == "3":   
             print(Flashcards)
        elif answer == "4":
            print("Incorrect answer")
        elif answer == "Q":   
            break
action()