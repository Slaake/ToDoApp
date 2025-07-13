import csv
import os

FileName = ""
List = []
MenuChoice = 0

def MainMenu():
    global MenuChoice
    print()
    print("\tWelcome to the Slaake Todo List.\n")
    while MenuChoice != 6:
        print("(1) Create a new ToDo List")
        print("(2) Add item to a ToDo List")
        print("(3) Remove item to a ToDo List")
        print("(4) Delete a ToDo List")
        print("(5) View All Lists")
        print("(6) Quit the Slaake ToDo Program\n")
        MenuChoice = input('Please select what you would like to do today: ')
        if MenuChoice < '1' or MenuChoice > '6':
            print("Please enter a valid choice from the menu.")
        else:
            return MenuChoice

def NewToDoListFile():
    global FileName
    FileName = input("\tPlease title your ToDo List File?\n")
    FileName = FileName + ".csv"
    try:
        with open(FileName, 'x') as file:
            print("Created a new file called " +FileName)
            return FileName
    except FileExistsError:
        print("That file name already exists\n")
        NewToDoListFile()

def CreateToDoList(File):
    global List
    ListName = input("\tWhat would you like to name your new list?\n")
    if ListName not in List:
        List.append(ListName)
    with open(File, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows([List])

def AddItemToList():
    print("\tAvailable Lists to add items to")
    print("\n".join(ToDoList))

def main():
    NewToDoListFile()
    CreateToDoList(FileName)

if __name__ == "__main__":
    main()
