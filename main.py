from src.GameItem import GameItem
import json
from os import path
import config

item = GameItem('Something')
item.printItem()


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
  inputStr = input('What would you like to do? ("exit" to close): ')
  if inputStr == 'exit':
    exitIndicated = True
