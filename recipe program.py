def action():
    global recipes
    recipes ={}
    while True:
        answer = input("What would you like to do :-\n"
                       "r) Read recipe\n"
                       "b) Add new recipe\n"
                       "n) Create a new recipe\n"
                       "l) List existing recipes\n"
                       "qq) Quit\n\n")

        if answer == "R" :
            print(recipes.values())
        elif answer == "c":
            name =str(input("\nWhat is the name of the food recipe you would like to create ? :- \n"))
            ingredients= str(input("\nWhat are the ingredients required to prepare this meal :- \n"))
            method =str(input('\nHow is the meal prepared :- \n'))
            recipes[name]=[name,ingredients,method]
            print(recipes[name])
        elif answer == "Q|q":
            break
action()