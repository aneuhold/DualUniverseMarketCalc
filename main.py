from src.GameItem import GameItem
from src.printFunctions import *
import json
from os import path
import config


def getGameItems():
  if path.exists(config.gameItemsFileName):
    with open(config.gameItemsFileName) as json_file:
      return json.load(json_file)
  else:
    return {}


# Import the items from a local json file if there is one
items = getGameItems()
print(items)

exitIndicated = False
while exitIndicated is False:
  inputStr = input('What would you like to do? ("help" for commands): ')
  if inputStr == 'exit':
    exitIndicated = True
  elif inputStr == 'help':
    printHelp()
