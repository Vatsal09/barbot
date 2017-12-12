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
from gpiozero import *
from time import sleep
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

### HARDWARE DEFINITIONS ###

motor1 = LED(17) # Vodka
motor2 = LED(27) # Tequila
motor3 = LED(22) # Margarita Mix
motor4 = LED(23) # Cranberry
# By default they are active high so we turn them off until ready
motor1.off()
motor2.off()
motor3.off()
motor4.off()

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
    # Counters 
    halfCount= 12319
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    # Normal Strength
    if (select2 == "Normal"):

    	if(select == "Margarita"):
	    	counter2 = halfCount*2 #1 oz teq
	    	counter3 = halfCount*6 #3 oz marg mix
	    	while True: 
		    	try:
		    		if(counter2 != 0):
		    			motor2.on()
		    			counter2 = counter2 - 1
		    		
		    			
		    		if(counter3 != 0):
		    			motor3.on()
		    			counter3 = counter3 - 1
		    		
		    		
		    		sleep(0.001)
		    		motor2.off()
		    		motor3.off()
		    		sleep(0.001)

		    		if(counter2 == 0 && counter3 ==0):
		    			counter1 = 0
		    			counter2 = 0
		    			counter3 = 0
		    			counter4 = 0
		    			motor2.off()
		    			motor3.off()
		    			break

		    	except KeyboardInterrupt:
		    		print("Catch 1")


		if(select == "Vodka-Cranberry"):
			counter1 = halfCount*2 #1 oz vodka
	    	counter4 = halfCount*9 #4.5 oz cranberry
	    	while True:
		    	try:
		    		if(counter1 != 0):
		    			motor1.on() #vodka
		    			counter1 = counter1 - 1
		    		
		    			
		    		if(counter4 != 0):
		    			motor4.on() #cranberry
		    			counter4 = counter4 - 1
		    		
		    		
		    		sleep(0.001)
		    		motor1.off()
		    		motor4.off()
		    		sleep(0.001)
		    		if(counter1 == 0 && counter4 ==0):
		    			counter1 = 0
		    			counter2 = 0
		    			counter3 = 0
		    			counter4 = 0
		    			motor1.off()
		    			motor4.off()
		    			break

		    	except KeyboardInterrupt:
		    		print("Catch 2")


	    if(select == "Winter Tropic"):
	    	counter1 = halfCount*3 #1.5 oz vodka
	    	counter3 = halfCount*3 #1.5 oz marg mix
	    	counter4 = halfCount*3 #1.5 oz cranberry
	    	while True:
		    	try:
		    		if(counter1 != 0):
		    			motor1.on() #vodka
		    			counter1 = counter1 - 1
		    		
		    		if(counter3 != 0):
		    			motor1.on() #marg mix
		    			counter1 = counter1 - 1

		    		if(counter4 != 0):
		    			motor4.on() #cranberry
		    			counter4 = counter4 - 1
		    		
		    		
		    		sleep(0.001)
		    		motor1.off()
		    		motor3.off()
		    		motor4.off()
		    		sleep(0.001)
		    		if(counter1 == 0 && counter4 ==0):
		    			counter1 = 0
		    			counter2 = 0
		    			counter3 = 0
		    			counter4 = 0
		    			motor1.off()
		    			motor3.off()
		    			motor4.off()
		    			break

		    	except KeyboardInterrupt:
		    		print("Catch 3")

	    if(select == "Vodarita"):
	    if(select == "Tequila Sunrise"):
	    if(select == "Tequila Shot"):
	    if(select == "Vodka Shot"):
	    if(select == "Scarlet Knight Shot"):


    if(select2 == "Extra Boozy"):

    	if(select == "Margarita"):

    	if(select == "Vodka-Cranberry"):

    	if(select == "Winter Tropic"): 

    	if(select == "Tequila Sunrise"):
    	if(select == "Vodarita" ):
    	if(select == "Tequila Shot"):
    	if(select == "Vodka Shot"):
    	if(select == "Scarlet Knight Shot"):



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

