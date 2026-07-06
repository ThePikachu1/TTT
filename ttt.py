"""A tic-tac-toe game built with Python and Tkinter."""
from tkinter import * 
from tkinter import messagebox
import string

# tkinter is a module which comes preinstalled with the python library
root = Tk() ## instantiate an instance of a window
root.title('Fathimas  - Tic Tac Toe')
## to set size of the window us the geometry function width * height
#root.geometry("420x420")

# the image right now is png format, tkinter only works with converted format 
# see below for example
# idk why this doesnt display the icon tho
icon = PhotoImage(file = 'UTD.png')
root.iconphoto(True, icon)
# bg color
root.config(background='pink') # or look up a hex color picker and include the #

# X goes first : so create a variable to keep track of whether X clicks or not 
clicked = True
moves = 0 
tie = False

global b1, b2, b3, b4,b5,b6,b7,b8,b9

# function b_click
def b_click(b):
    global clicked, moves
    flag = 0
    if(b["text"] == ' ' and clicked == True):
        b["text"] = 'X'
        clicked = False
        moves += 1
        flag = 1
    elif(b["text"]== ' ' and clicked == False):
        b["text"] = 'O'
        clicked = True
        moves += 1
        flag = 1
    elif(b["text"] != ' '):
        ## player trying to access filled square => not allowed => display message
        messagebox.showerror('Box occupied', message = "Box already filled!\n Play elsewhere")

    if(flag == 1):
        checkWinner()
        flag = 0

# creating the reset game function
def reset():
    global b1, b2, b3, b4,b5,b6,b7,b8,b9
    global clicked , moves
    clicked = True
    count = 0 
    # create buttons and alot them locations using .grid() ie grid each button to the screen
    b1 = Label(root, text=" ", width=5, height=3, relief = "raised", pady = 30, padx= 30)
    b1.bind("<Button-1>", lambda e: b_click(b1))
    b1.grid(row= 0 , column=0)

    b2 = Label(root, text=" ", width=5, height=3, relief="raised", pady = 30, padx= 30)
    b2.bind("<Button-1>", lambda e: b_click(b2))
    b2.grid(row= 0 , column=1)

    b3 = Label(root, text=" ", width=5, height=3, relief="raised", pady = 30, padx= 30)
    b3.bind("<Button-1>", lambda e: b_click(b3))
    b3.grid(row= 0 , column=2)

    b4 = Label(root, text=" ", width=5, height=3, relief="raised", pady = 30, padx= 30)
    b4.bind("<Button-1>", lambda e: b_click(b4))
    b4.grid(row = 1, column= 0)

    b5 = Label(root, text=" ", width= 5, height=3 , relief="raised", pady = 30, padx= 30)
    b5.bind("<Button-1>", lambda e: b_click(b5))
    b5.grid(row = 1, column= 1)

    b6 = Label(root, text=" ", width= 5, height=3 , relief="raised", pady = 30, padx= 30)
    b6.bind("<Button-1>", lambda e: b_click(b6))
    b6.grid(row = 1, column= 2)

    b7 = Label(root, text=" ", width= 5, height=3 , relief="raised", pady = 30, padx= 30)
    b7.bind("<Button-1>", lambda e: b_click(b7))
    b7.grid(row = 2, column= 0)

    b8 = Label(root, text=" ", width= 5, height=3 , relief="raised", pady = 30, padx= 30)
    b8.bind("<Button-1>", lambda e: b_click(b8))
    b8.grid(row = 2, column= 1)

    b9 = Label(root, text=" ", width= 5, height=3 , relief="raised", pady = 30, padx= 30)
    b9.bind("<Button-1>", lambda e: b_click(b9))
    b9.grid(row = 2, column= 2)


def disable_all_buttons():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)
    global clicked, moves
    moves = 0 
    clicked = True
    
## function to check if win or tie

def checkWinner():
    global winner , tie , line
    winner = False
    tie = False
    
    if(b1["text"] == b2["text"]== b3["text"]!=' '):
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        winner = True
        root.update()
        messagebox.showinfo(message="Congo! " + b1["text"] + " wins!")
    elif(b4["text"] == b5["text"]== b6["text"]!=' '):
        b4.config(bg='red')
        b5.config(bg='red')
        b6.config(bg='red')
        winner = True
        root.update()
        messagebox.showinfo('Winner', message = "Congratulations!"+ b4["text"] +" wins!")
    elif(b7["text"] == b8["text"]== b9["text"]!=' '):
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        root.update()
        messagebox.showinfo('Winner', message = "Congratulations!"+ b7["text"] +" wins!")
    elif(b1["text"] == b5["text"]== b9["text"]!=' '):
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        root.update()
        messagebox.showinfo('Winner', message = "Congratulations!"+ b5["text"] +" wins!")
    elif(b3["text"] == b5["text"]== b7["text"]!=' '):
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        root.update()
        messagebox.showinfo('Winner', message = "Congratulations!"+ b5["text"] +" wins!")
    elif(b1["text"] == b4["text"]== b7["text"]!=' '):
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        root.update()
        messagebox.showinfo('Winner', message = "Congratulations!"+ b4["text"] +" wins!")
    elif(b2["text"] == b5["text"]== b8["text"]!=' '):
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        root.update()
        messagebox.showinfo('Winner', message = "Congratulations!"+ b5["text"] +" wins!")
    elif(b3["text"] == b6["text"]== b9["text"]!=' '):
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        root.update()
        messagebox.showinfo('Winner', message = "Congratulations!"+ b5["text"] +" wins!")
    elif(moves ==9 and winner == False):
        tie = True
        messagebox.showinfo(message="Game tied!")
        

    if winner or tie:
        disable_all_buttons()


    return False

  

## creating a menu to reset the the game to be able to play it again
my_menu = Menu(root)
root.config(menu = my_menu)

## adding options to the menu
options_menu = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label = "Options", menu = options_menu)
options_menu.add_command(label = "Reset Game", command = reset)

reset()

root.mainloop() ## to display the window and listens for events 