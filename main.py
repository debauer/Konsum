#!/usr/bin/env python3 
import os, sys, time, _thread
from getkey import getkey, keys

try:
  from termcolor import colored
except ImportError:
  NO_COLOR = True
else:
  NO_COLOR = False

width = 120

identDefault = {"authed": False, "name": "¯x_(ツ)_/¯ ", "gold": 0.0}
identMock = {"authed": True, "name": "David", "gold": 13.37}

lastTransactionGoods = []
timeOutDefault = 300
timeOut = timeOutDefault
inputStr = ""
infoStr = ""
debugStr = ""
focusId = -1

ident = identDefault
session = {"cart": [], "lastTransactionGoods": [], "shortCart": []}

goods = []
goods.append({"name": "0.10 Gold einzahlen",  "gold": -0.1})
goods.append({"name": "1 Gold einzahlen",  "gold": -1})
goods.append({"name": "10 Gold einzahlen",  "gold": -10})
goods.append({"name": "Premium Cola",  "gold": 0.33})
goods.append({"name": "Premium Fanta", "gold": 0.77})
goods.append({"name": "Fritz Cola", "gold": 0.77})
goods.append({"name": "Fritz Orange", "gold": 0.77})
goods.append({"name": "Fritz Pfirsich", "gold": 0.77})
goods.append({"name": "Fritz Apfel", "gold": 0.77})
goods.append({"name": "Warsteiner", "gold": 0.77})
goods.append({"name": "Becks", "gold": 0.77})
goods.append({"name": "Rothaus", "gold": 0.77})
goods.append({"name": "Krümel", "gold": 0.77})
goods.append({"name": "Kaka", "gold": 0.77})
goods.append({"name": "Geschirr", "gold": 0.77})
goods.append({"name": "Lukas3", "gold": 0.77})

def reset():
	global ident, colors
	colors = colorDefault
	ident = identDefault
	session["cart"].clear()
	session["cart"] = goods.copy()
	for s in session["cart"]:
		s["amount"] = 0
		s["touched"] = False
	lastTransactionGoods.clear()

def logout():
	reset()

def login():
	global ident, colors
	colors = colorAuthed
	ident = identMock


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
	print()

def status():
	print(color2(str(timeOut)))

def footer():
	print()
	print(line("―"))
	if ident["authed"]:
		print(color3(" letzter Kuhhandel:")+ " vorgestern 1x Getränke, 2x Süßkram für " 
					 + gold('%6s' % str(22.22) + "€", -22.22))
		print(color3(" dein Goldspeicher: ") + gold(str(ident["gold"]) + "€", ident["gold"]) +"  | AVG: " 
					 + str(23.42) +"€ day "  
					 + str(2.00) +"€ week " 
					 + str(23.2) +"€ month")
	else:
		l = width/2 - 14
		print((" "*int(l)) + red("nicht zu erkennen gegeben!") + (" "*int(l)) )
		print((" "*int(l)) + red("nicht zu erkennen gegeben!") + (" "*int(l)))
	print(line("―"))

def getIndexOfArray(index, array):
	if index >= len(array):
		return {"name":"", "amount": 0}
	return array[index]

def getCartList():
	i = 0
	data = []
	for s in session["cart"]:
		if s["amount"] != 0:
			data.append(s)
	while i < 10:
		data.append(False)
		i=i+1
	return data

def getCartAmount():
	a = 0
	for s in session["cart"]:
		a = a + (s["amount"] * s["gold"])
	return a


def body():
	global focusId
	print(headline(" verfügbare Konsumgüter") + " " * 52 + headline("Konsumkorb ")+gold("["+str(getCartAmount())+"]",getCartAmount()*-1)+headline(":"))
	lines = 15
	rows = 10
	cartList = getCartList()
	print()
	for i in range(0,rows):
		c1 = " " + '%2s' % str(i) + ": " + '%-20s' % getIndexOfArray(i,goods)["name"]
		c2 = " " + '%2s' % str(rows+i) + ": " + '%-20s' % getIndexOfArray(rows+i,goods)["name"]
		c3 = " " + '%2s' % str(2*rows+i) + ": " + '%-20s' % getIndexOfArray(2*rows+i,goods)["name"]
		if cartList[i]:
			c4 = " " + str(cartList[i]["amount"]) + "x "+ '%-20s' % cartList[i]["name"] 
		else:
			c4 = ""
		if i == focusId: c1 = color3(c1)
		if rows+i == focusId: c2 = color3(c2)
		if 2*rows+i == focusId: c3 = color3(c3)
		print(c1+c2+c3+c4)
	print()

def printInput():
	global inputStr, infoStr
	print(color3(" Info: ") + infoStr)
	print(color3(" Input: ") + inputStr)

def auth():
	# clear screen
	printFlush("Geben Sie sich zu erkennen!")
	name = input("Name: ")
	pin = input("Pin: ")
	#check auth
	return {"authed": True, "id": 7, "name": name, }

def removeGoodfromCart(id):
	global session, debugStr
	session["cart"][id]["amount"] = session["cart"][id]["amount"] - 1
	session["cart"][id]["touched"] = True

def addGoodToCart(id):
	global session, debugStr
	session["cart"][id]["amount"] = session["cart"][id]["amount"] + 1
	session["cart"][id]["touched"] = True

	# build shortCart

def inputHandler(command):
	global infoStr, focusId
	try:
		i = int(inputStr)
		if command == "add":
			infoStr = "Konsumgut "+str(i)+" hinzugefügt"
			addGoodToCart(i)
		if command == "sub":
			infoStr = "Konsumgut "+str(i)+" entfernt"
			removeGoodfromCart(i)
		else:
			focusId = i
	except ValueError:
		focusId = -1
		#infoStr = "nicht erkannt"
		pass


def keyHandler():
	global inputStr, timeOut, timeOutDefault, focusId
	try:
		while True:
			time.sleep(0.01)
			key = getkey()
			if key == "-" or key == "_":
				inputHandler("sub")
			elif key == "+" or key == "*":
				inputHandler("add")
				#inputStr = "" # lieber mal drin lassen für mehrfach kauf
				#focusId = -1 # same as above
			elif key == "q" or key == "Q":
				os._exit(1)
			elif key == "b" or key == "B":
				#inputStr = "barcode!"
				pass
			elif key == "r" or key == "R":
				#inputStr = "RFID!"
				pass
			elif key == "l" or key == "L":
				#inputStr = "RFID!"
				login()
				pass
			elif key == "c" or key == "C":
				#focusId = -1
				inputStr = inputStr[:-1]
			elif key == "0" or key == "1" or key == "2"or key == "3"or key == "4"or key == "5"or key == "6" or key == "7" or key == "8" or key == "9":
				inputStr = inputStr + key

			if key != "":
				inputHandler(False)
				timeOut = timeOutDefault
	except Exception as e:
		print (e)
		os._exit(1)

def timeOutHandler():
	global timeOut
	if timeOut:
		timeOut = timeOut - 1
	if(timeOut <= 0):
		logout()

reset()
ident = identMock
colors = colorAuthed
_thread.start_new_thread(keyHandler, ())
if __name__ == '__main__':
	while True:
		clear()
		#colors = colorError
		header()
		body()
		printInput() # lines
		footer() # 4 lines
		status()
		print(debugStr)
		time.sleep(0.1)
		timeOutHandler()
		
		
