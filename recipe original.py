def action():
    global recipes
    recipes ={}
    while True:
        answer = input("Select from the Menu \n"
                       "N.) Add new recipe\n"
                       "L.) List existing recipes\n"
                       "R.) Read recipe\n"
                       "Q.) Quit\n\n")
                      
    
                       
         
        if answer == "L" :
            print(recipes.values())
        elif answer == "N":           
            name =str(input("\nWhat recipe would you would like to make ?  \n"))
            ingredients= str(input("\nWhat are the ingredients for the recipe  \n"))
            method =str(input('\nHow is the meal prepared  \n'))
            recipes[name]=[name,ingredients,method]
            print(recipes[name])
        elif answer == "R":   
             print(recipes)
        elif answer == "Q":
            break
action()