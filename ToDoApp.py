# Create a new ToDo List
# Add item to list
# Remove item from list
# Delete list
# View lists

MenuChoice = '0'
ListName = []

def MainMenu():
    global MenuChoice
    print()
    print("\tWelcome to the Slaake Todo List.")
    while MenuChoice != 6:
        print()
        print("(1) Create a new ToDo List")
        print("(2) Add item to a ToDo List")
        print("(3) Remove item to a ToDo List")
        print("(4) Delete a ToDo List")
        print("(5) View All Lists")
        print("(6) Quit the Slaake ToDo Program")
        print()
        MenuChoice = input('Please select what you would like to do today: ')
        print()

        if MenuChoice < '1' or MenuChoice > '6':
            print("Please enter a valid choice from the menu.")
        else:
            return MenuChoice

def ToDoLists(MenuChoice):
    if MenuChoice == '1':
        print("\tCreating a new List")
        ListName = input("Enter name for the list: ")
        while ListName == "":
            print("Please name your list")
            ListName = input("Enter name for the list: ")
        else:
            print(ListName, "has been created.")
        
        print("Would you like to make another list?")


if __name__ == '__main__':
    MainMenu()
    ToDoLists(MenuChoice)
