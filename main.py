#!/usr/bin/env python3 
import os, sys
try:
  from termcolor import colored
except ImportError:
  noColor = True
else:
  noColor = False

manMoegeBildschirmSaeubern = lambda: os.system('clear')

liquids = []

liquids.append({"rang": 1, "benamsung": "Premium Cola", "gold": 0.33})
liquids.append({"rang": 2, "benamsung": "Premium Fanta", "gold": 0.77})

def aeusernSieInFarbe(t,tc, o, oc):
    if noColor:
        printFlush (t + o)
    else:
        printFlush (colored(t, tc) + colored(o, oc))

def aeusernSieDirekt(msg):
    print(msg)
    sys.stdout.flush()

def gebeLiquidsAus():
	for l in liquids:
		aeusernSieInFarbe(str(l["rang"]),'cyan', ": " + l["benamsung"] + " kostet " + str(l["gold"]), 'white')

def wieIstIhrName():
	# clear screen
	manMoegeBildschirmSaeubern()
	aeusernSieDirekt("wie ist ihr Name werter Herr?")
	eingabe = input("-> ")
	aeusernSieDirekt(eingabe) 

	# input

if __name__ == '__main__':
	wieIstIhrName()
	gebeLiquidsAus()