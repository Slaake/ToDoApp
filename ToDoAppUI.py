# Tkinter configuration files

from customtkinter import *
from tkinter import *
from ToDoApp import *

# Init Variables
HomeWindow = Tk()

HomeWindow.geometry('450x450')
HomeWindow.title('ToDo App')
icon = PhotoImage(file='logo.png')
HomeWindow.iconphoto(True,icon)
HomeWindow.config(background='grey')

# App Window
label = Label(HomeWindow,
                text='To-Do App',
                font=('hack mono',35,'bold'),
                fg='black',
                bg='grey',
                relief=GROOVE,
                bd=10,
                padx=10,
                pady=10,
                image=icon,
                compound='left',
            )

# Action Buttons
NewListButton = Button(HomeWindow,
                text="Create a new list",
                font=('hack mono',20),
                fg='black',
                bg='grey',
                activeforeground='black',
                activebackground='grey',
                command=CreateToDoList,
                )

UpdateListButton = Button(HomeWindow,
                text="Update a list",
                font=('hack mono',20),
                fg='black',
                bg='grey',
                activeforeground='black',
                activebackground='grey',
                command=MainMenu,
                )

DeleteListButton = Button(HomeWindow,
                text="Delete a list",
                font=('hack mono',20),
                fg='black',
                bg='grey',
                activeforeground='black',
                activebackground='grey',
                command=MainMenu,
                )
ViewListButton = Button(HomeWindow,
                text="View a list",
                font=('hack mono',20),
                fg='black',
                bg='grey',
                activeforeground='black',
                activebackground='grey',
                command=MainMenu,
                )

# User Input Box
UserInput = Entry(HomeWindow,
            font=('hack mono',20))

label.pack()
UserInput.pack()
NewListButton.pack()
UpdateListButton.pack()
DeleteListButton.pack()
ViewListButton.pack()
UserInput.pack()

HomeWindow.mainloop()

