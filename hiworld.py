# hiworld.py - first python program from Alex Ward.
# Some tkinter revisions by DaleEMoore@gMail.Com

# From: https://wiki.python.org/moin/Intro%20to%20programming%20with%20Python%20and%20Tkinter



# lecture3 example 1
from Tkinter import *           # Importing the Tkinter (tool box) library
root = Tk()                     # Create a background window
                                # Create a list
li = 'Carl Patrick Lindsay Helmut Chris Gwen'.split()
listb = Listbox(root)           # Create a listbox widget
for item in li:                 # Insert each item within li into the listbox
    listb.insert(0,item)

listb.pack()                    # Pack listbox widget
root.mainloop()                 # Execute the main event handler



# lecture3 example 2
from Tkinter import *           # Import the Tkinter library
root = Tk()                    # Create a background window object
                                # A simple way to create 2 lists
li     = ['Carl','Patrick','Lindsay','Helmut','Chris','Gwen']
movie  = ['God Father','Beauty and the Beast','Brave heart']
listb  = Listbox(root)          # Create 2 listbox widgets
listb2 = Listbox(root)
for item in li:                 # Insert each item inside li into the listb
    listb.insert(0,item)

for item in movie:              # Do the same for the second listbox
    listb2.insert(0,item)

listb.pack()                    # Pack each listbox into the main window
listb2.pack()
root.mainloop()                 # Invoke the main event handling loop



#lecture4 example 1
from Tkinter import *

def Pressed():                          #function
        print 'buttons are cool'

root = Tk()                             #main window
button = Button(root, text = 'Press', command = Pressed)
button.pack(pady=20, padx = 20)
Pressed()
root.mainloop()



# lecture4 example 2
# Souce section   1
# mandatory for unix and linux
# ---------------------------------------------------------------
from Tkinter import *  # This library give us windows and buttons
from random import *  # This library allows us to generate random numbers
# import library section   2
#
# What not to use???
# ---------------------------------------------------------------
def one_to_ten():
    ran = uniform(1, 10)
    print ran
def GoWork():  # def starts a function, or define a function
    sum = 3 * 5
    print sum  # Function section   3
# ----------------------------------------------------------------
# Code section    4
window = Tk()  # i am the parent, button = child
stacy = Button(window, text='yoyo', command=one_to_ten)
# A rose with any other name would be just as sweet
stacy.pack()  # you can name it after your fish (ignored)
window.mainloop()  # you can use your fish's name



# lecture4 example 3
from Tkinter import *

def Call():
        lab= Label(root, text = 'You pressed\nthe button')
        lab.pack()
        button['bg'] = 'blue'
        button['fg'] = 'white'

root = Tk()
root.geometry('100x110+350+70')
button = Button(root, text = 'Press me', command = Call)
button.pack()

root.mainloop()



# lecture4 example 5
from Tkinter import *  # This interface allow us to draw windows
def DrawList():
    plist = ['Liz', 'Tom', 'Chi']

    for item in plist:
        listbox.insert(END, item);
root = Tk()  # This creates a window, but it won't show up

listbox = Listbox(root)
button = Button(root, text="press me", command=DrawList)

button.pack()
listbox.pack()  # this tells the listbox to come out
root.mainloop()  # This command will tell the window come out



# hiworld2.py
print("Hi there world.") # python3 syntax, works in python2 also.
print "Hi World" # python2 syntax, doesn't work in python3.



# Original attempt
#"echo" HiWorld