import json
from os import path
from src.GameItem import GameItem
import jsonpickle

gameItemsFileName = '../gameItems.json'


class GameItems:
  """Holds the different game items and allows them to be interacted with."""

  def __init__(self):
    if path.exists(gameItemsFileName):
      with open(gameItemsFileName) as json_file:
        self._gameItems = jsonpickle.decode(json_file.read())
    else:
      self._gameItems = {}

  def addItem(self, name):
    if name in self._gameItems:
      print('The item with the name ' + name + ' already exists.')
      return False
    else:
      self._gameItems[name] = GameItem(name)
      self.save()
      return True

  def getItem(self, name):
    return self._gameItems[name]

  def getItems(self):
    return self._gameItems

  def save(self):
    with open(gameItemsFileName, 'w') as json_file:
      json_file.write(jsonpickle.encode(self._gameItems))