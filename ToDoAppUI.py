# Tkinter configuration files

from tkinter import *
from ToDoApp import *

window = Tk()
window.geometry('450x450')
window.title('ToDo App')
icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)
window.config(background='grey')

label = Label(window,
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

button = Button(window,
                text="Create a new list",
                font=('hack mono',20),
                fg='black',
                bg='grey',
                activeforeground='black',
                activebackground='grey',
                command=MainMenu,
                )

label.pack()
button.pack()

window.mainloop()

