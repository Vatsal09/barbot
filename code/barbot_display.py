# BarBot Display UI

# Based on research, margarita is the most popular/requested drink at bars

# (Link 1) <https://www.bevindustry.com/articles/89307-margarita-ranks-most-popular-cocktail-in-the-us-nielsen-cga-survey-finds>
# (Link 2) <http://www.brakesce.co.uk/pages/multimedia/db_document.document?id=4088>

# 4 bottles: Tequila, Margarita Mix, Vodka, Cranberry 
# List:
# Tequila Shot (1.5 oz tequila) - Size: 1.5
# Vodka Shot (1.5 oz vodka) - Size: 1.5
# Margarita (1 oz tequila, 3 oz marg mix) - Size: 12
# Winter Tropic (1.5 oz vodka, 1.5 oz cranberry, 1.5 oz marg mix) - Size: 12
# Vodka-Cranberry (1 oz vodka, 4.5 oz cranberry) - Size: 10
# Tequila Sunrise (4 oz cranberry, 1.5 oz tequila) - Size: 10
# Vodarita (1.5 oz vodka, 3 oz marg mix) - Size: 10
# Scarlet Knight Shot (1.5 oz vodka, 0.5 oz marg mix) - Size: 2

### IMPORTS

from tkinter import *
import tkinter.font

### GUI DEFINITIONS ###

win = Tk()
win.title("BarBot Drink Selection")
titleFont = tkinter.font.Font(family = 'Helvetica', size = 16, weight = "bold")
subTitleFont = tkinter.font.Font(family = 'Helvetica', size = 13, weight = "bold")
elementFont =  tkinter.font.Font(family = 'Helvetica', size = 11)
subFont =  tkinter.font.Font(family = 'Helvetica', size = 9)
leftFrame = Frame(win)
leftFrame.pack(side = LEFT, fill=BOTH, expand =1, anchor = W)
rightFrame = Frame(win)
rightFrame.pack(side = RIGHT, fill=BOTH, expand =1, anchor = W)

### VARIABLE DEFINTIONS ###

checkVal1 = StringVar()
checkVal1.set("L")
checkVal2 = StringVar()
checkVal2.set("L")

## EVENT TRIGGERS ###

def checkRadio():
    return "Radio button " + str(checkVal1.get()) + " selected"

def buttonPress():
    select = checkRadio()
    select2 = checkRadio2()
    print(select + "\n" + select2)
def checkRadio2():
    return "Radio button " + str(checkVal2.get()) + " selected"


### WIDGETS ###

# Radio Buttons for Drink Type

label1 = Label(leftFrame, text= "Cocktails: ", font= subTitleFont)
label1.pack(fill = BOTH, expand =1, anchor=W)
R1 = Radiobutton(leftFrame, text="Margarita", variable=checkVal1,value="Margarita", command = checkRadio, font = elementFont, pady= 8)
R1.pack(fill = BOTH, expand =1, anchor=W)
R2 = Radiobutton(leftFrame, text="Vodka-Cranberry",variable=checkVal1,value="Vodka-Cranberry", command = checkRadio, font = elementFont, pady= 8)
R2.pack(fill = BOTH, expand =1, anchor=W)
R3 = Radiobutton(leftFrame, text="Winter Tropic",variable=checkVal1,value="Winter Tropic", command = checkRadio, font = elementFont, pady= 8)
R3.pack(fill = BOTH, expand =1, anchor=W)
R4 = Radiobutton(leftFrame, text="Tequila Sunrise",variable=checkVal1,value="Tequila Sunrise", command = checkRadio, font = elementFont, pady= 8)
R4.pack(fill = BOTH, expand =1, anchor=W)
R5 = Radiobutton(leftFrame, text="Vodarita",variable=checkVal1,value="Vodarita", command = checkRadio, font = elementFont, pady= 8)
R5.pack(fill = BOTH, expand =1, anchor=W)
label2 = Label(leftFrame, text= "\nShots: ", font= subTitleFont)
label2.pack(fill = BOTH, expand =1, anchor=W)
R6 = Radiobutton(leftFrame, text="Tequila Shot",variable=checkVal1,value="Tequila Shot", command = checkRadio, font = elementFont, pady= 8)
R6.pack(fill = BOTH, expand =1, anchor=W)
R7 = Radiobutton(leftFrame, text="Vodka Shot",variable=checkVal1,value="Vodka Shot", command = checkRadio, font = elementFont, pady= 8)
R7.pack(fill = BOTH, expand =1, anchor=W)
R8 = Radiobutton(leftFrame, text="Scarlet Knight Shot",variable=checkVal1,value="Scarlet Knight Shot", command = checkRadio, font = elementFont, pady= 8)
R8.pack(fill = BOTH, expand =1, anchor=W)

# Radio Buttons for Drink Strength

label3 = Label(rightFrame, text= "Strength of Drink: ", font= subTitleFont)
label3.pack(fill = BOTH, anchor=W)
R9 = Radiobutton(rightFrame, text="Normal", variable=checkVal2,value="Normal", command = checkRadio2, font = elementFont, pady= 4)
R9.pack(fill = BOTH, anchor=W)
R10 = Radiobutton(rightFrame, text="Extra Boozy",variable=checkVal2,value="Extra Boozy", command = checkRadio2, font = elementFont, pady=4)
R10.pack(fill = BOTH, anchor=W)

# Start Button

startButton = Button(rightFrame, text='Start', font=titleFont, command=buttonPress, bg='green', fg='white', height=1)
startButton.pack(fill = BOTH, pady = 15)

win.mainloop() # Loops forever

