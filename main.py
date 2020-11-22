from src.GameItems import GameItems
from src.printFunctions import *
import json
from os import path
import config

gameItems = GameItems()


def addGameItem():
  name = input('Name of the game item: ')
  addResult = gameItems.addItem(name)
  if (addResult is not True):
    return
  print('Game item addition was successful')


def printItems():
  gameItems.printItems()


def editGameItem(name):
  gameItem = gameItems.getItem(name)
  if (gameItem is None):
    return
  print('found the item')


exitIndicated = False
while exitIndicated is False:
  inputStr = input('What would you like to do? ("help" for commands): ')
  if inputStr == 'exit':
    exitIndicated = True
  elif inputStr == 'help':
    printHelp()
  elif inputStr == 'add':
    addGameItem()
  elif inputStr == 'print':
    printItems()
  elif inputStr.startswith('edit'):
    editGameItem(inputStr[5:])
