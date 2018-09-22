#!/usr/bin/env python3 
import os, sys, time
try:
  from termcolor import colored
except ImportError:
  NO_COLOR = True
else:
  NO_COLOR = False

width = 120

identDefault = {"authed": False, "name": "¯x_(ツ)_/¯ ", "gold":0.0}
identMock = {"authed": True, "name": "David", "gold":13.37}
ident = identDefault
choosengoods = []
lastTransactionGoods = []
timeOut = 50

def reset():
	global ident, colors
	colors = colorDefault
	ident = identDefault
	choosengoods.clear()
	lastTransactionGoods.clear()

def logout():
	
	reset()

goods = []
goods.append({"rang": 1, "name": "Premium Cola", "gold": 0.33})
goods.append({"rang": 2, "name": "Premium Fanta", "gold": 0.77})
goods.append({"rang": 3, "name": "Premium Fanta", "gold": 0.77})
goods.append({"rang": 4, "name": "Premium Fanta", "gold": 0.77})
goods.append({"rang": 5, "name": "Premium Fanta", "gold": 0.77})
goods.append({"rang": 6, "name": "Premium Fanta", "gold": 0.77})
goods.append({"rang": 7, "name": "Premium Fanta", "gold": 0.77})
goods.append({"rang": 8, "name": "Premium Fanta", "gold": 0.77})
goods.append({"rang": 9, "name": "Premium Fanta", "gold": 0.77})

colorDefault = {"color1": "white", 
				"color2": "grey",
				"color3": "cyan",  
				"text": "white", 
				"parameter": "magenta", 
				"spacer": "white", 
				"spacer_attr": [], 
				"headline": "magenta"}
colorAuthed = {"color1": "white", "color2": "grey","color3": "cyan","text": "white", "parameter": "magenta", "spacer": "green", "spacer_attr": [], "headline": "magenta"}
colorError = {"color1": "white", "color2": "grey","color3": "cyan","text": "white", "parameter": "magenta", "spacer": "red", "spacer_attr": ["blink"], "headline": "magenta"}

colors = colorDefault

clear = lambda: os.system('clear')
line = lambda x: colored(width * x, colors["spacer"], attrs=colors["spacer_attr"])
pipe = lambda: colored("‖", colors["spacer"], attrs=colors["spacer_attr"])
text = lambda x: colored(x, colors["text"])
headline = lambda x: colored(x, colors["headline"])
parameter = lambda x: colored(x, colors["parameter"])
color1 = lambda x: colored(x, colors["color1"])
color2 = lambda x: colored(x, colors["color2"])
color3 = lambda x: colored(x, colors["color3"])
red = lambda x: colored(x, "red")
gold = lambda x, gold: colored(x, "red") if gold < 0 else colored(x, "green")

def printColor(t,tc, o, oc):
    if NO_COLOR:
        printFlush (t + o)
    else:
        printFlush (colored(t, tc) + colored(o, oc)) 

def printFlush(msg):
    print(msg)
    sys.stdout.flush()

def printAllgoods():
	for l in goods:
		printColor(str(l["rang"]),'cyan', ": " + l["name"] + " kostet " + str(l["gold"]), 'white')
	

def printChoosenLiquid():
	printFlush("Folgende Konsumierungs Gegenstände hast du ausgewählt: ")
	for l in choosengoods:
		printColor(str(l["rang"]),'cyan', ": " + l["name"] + " kostet " + str(l["gold"]), 'white')
	

def chooseLiquid():
	printFlush("hallo " + ident["name"] + " was möchtest du gerne Konsumieren?")
	printColor("00:",'cyan', " gold abliefern", 'white')
	for l in goods:
		printColor(str(l["rang"]),'cyan', ": " + l["name"] + " kostet " + str(l["gold"]), 'white')
	auswahl = input("Sag mir die Nummer: ")
	k = input("du möchstest gerne " + auswahl + " drinken? [j/n] ")
	if k == "j":
		choosengoods.append(goods[0])
		return True
	else:
		return False

def header():
	lenMinus2 = width-2
	textLoggedIn = "logged in: "
	print(line("―"))
	l = ((width - len(textLoggedIn) - len(ident["name"])) / 2)-2
	corr = len(ident["name"]) & 1 == 0
	if ident["authed"]:
		print(pipe() + (" "*int(l)) + text("logged in: "),parameter(ident["name"]) + (" "*int(l+corr)) + pipe())
	else:
		l = width/2 - 14
		print(pipe() + (" "*int(l)) + red("nicht zu erkennen gegeben!") + (" "*int(l)) + pipe())
	#print(pipe() + (" "*lenMinus2) + pipe())
	print(line("―"))

def footer():
	print(line("―"))
	if ident["authed"]:
		print(color3(" letzter Kuhhandel:")+ " vorgestern 1x Getränke, 2x Süßkram für " 
					 + gold('%6s' % str(22.22) + "€", -22.22))
		print(color3(" dein Goldspeicher: ") + gold(str(ident["gold"]) + "€", ident["gold"]) +"  | AVG: " 
					 + str(23.42) +"€ day "  
					 + str(2.00) +"€ week " 
					 + str(23.2) +"€ month" 
					 + "timeout:" + str(timeOut))
	else:
		l = width/2 - 14
		print((" "*int(l)) + red("nicht zu erkennen gegeben!") + (" "*int(l)) )
		print((" "*int(l)) + red("nicht zu erkennen gegeben!") + (" "*int(l)))
	print(line("―"))

def printInput():
	i = "asd"
	print("Input: " + i)

def auth():
	# clear screen
	printFlush("Geben Sie sich zu erkennen!")
	name = input("Name: ")
	pin = input("Pin: ")
	#check auth
	return {"authed": True, "id": 7, "name": name, }

reset()
ident = identMock
colors = colorAuthed
if __name__ == '__main__':
	while True:
		clear()
		#colors = colorError
		header()
		print()
		print(headline("verfügbare Konsumgüter"))
		printAllgoods()
		print()
		print()
		print()
		print()
		print()
		printInput()
		footer()
		time.sleep(0.1)
		timeOut = timeOut - 1
		if(timeOut < 0.0):
			logout()
