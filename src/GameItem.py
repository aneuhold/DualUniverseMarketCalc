from src.TermColors import Colors, colorText
from src.ItemData import ItemData
from src.inputUtils import parseToNum


class GameItemDataName:
  NAME = 'name'
  MARKET_SELL_PRICE = 'marketSellPrice'
  CRAFTING_COST = 'craftingCost'


class GameItem:
  """Represents an item in the game. Holds values for it's market value and
  sub-components"""

  def __init__(self, name):
    self._data = {
        GameItemDataName.NAME: ItemData('Name', name),
        GameItemDataName.MARKET_SELL_PRICE: ItemData('Market Sell Price', None),
        GameItemDataName.CRAFTING_COST: ItemData('Crafting Components', {})
    }

  def getData(self, dataName):
    """Gets the data associated with the given data name"""
    if dataName in self._data:
      return self._data[dataName]
    else:
      print('Property with name: ', dataName, ' was not found.')

  def setData(self, dataName, newData):
    """Sets the data for the item with the given name"""
    if dataName in self._data:
      self._data[dataName].data = newData
    else:
      print('Property with name: ', dataName, ' was not found.')

  def addCraftingCost(self, itemName, quantity):
    craftingCost = self._data.craftingCost.data
    craftingCost[itemName] = quantity
    self._data.craftingCost.data = craftingCost

  def editPrompt(self):
    dataKeyList = list(self._data.keys())
    doneEditing = False
    while (doneEditing is False):
      print('Enter a number from below to update its value')
      i = 1
      for key in dataKeyList:
        itemData = self._data[key]
        print(str(i) + '. ' + str(itemData.title) + ': ' + str(itemData.data))
        i += 1
      print(str(i) + '. Stop editing')
      choice = input('Enter a number from above: ')
      parsedChoice = parseToNum(choice, 1, dataKeyList.__len__() + 1)

      # If the choice was successfully parsed
      if (parsedChoice is not None):
        # If they chose to stop editing
        if (parsedChoice == dataKeyList.__len__() + 1):
          doneEditing = True
        else:
          self.editDataPrompt(dataKeyList[parsedChoice - 1])

  def editDataPrompt(self, dataName):
    if (dataName == GameItemDataName.CRAFTING_COST):
      self.editCraftingCostPrompt()
      return

    newValue = input('Enter a new value for "' + self._data[dataName].title + '": ')
    self._data[dataName].data = newValue
    print('Value successfully changed')

  def editCraftingCostPrompt(self):
    doneEditing = False
    while(doneEditing is False):
      print('Enter a command below to edit the crafting components')
      print(Colors.OKCYAN + 'add' + Colors.ENDC +
            ': Add a new crafting requirement to ' +
            colorText(self._data['name'].data, Colors.OKBLUE))
      print(Colors.OKCYAN + 'edit [itemName]' + Colors.ENDC +
            ': Edit the crafting requirement with the given ' +
            '"itemName"')
      print(Colors.OKCYAN + 'delete [itemName]' + Colors.ENDC +
            ' Delete the crafting requirement with the given' +
            ' "itemName"')
      print(Colors.OKCYAN + 'exit' + Colors.ENDC +
            ': Exit editing')
      inputStr = input('Enter command: ')
      if (inputStr == 'exit'):
        doneEditing = True
      elif (inputStr == 'add'):
        self.addCraftingCostPrompt()

  def addCraftingCostPrompt(self):
    name = input('Enter the name of the crafting component: ')
    parsedChoice = None
    while (parsedChoice == None):
      quantity = input('Enter the quantity of the crafting component: ')
      parsedChoice = parseToNum(quantity, 1)
      if (parsedChoice is not None):
        craftingItems = self._data[GameItemDataName.CRAFTING_COST].data
        craftingItems[name] = quantity
        self._data[GameItemDataName.CRAFTING_COST].data = craftingItems

  def print(self):
    """Prints values for this game item to the console"""
    print(Colors.OKBLUE + self._data['name'].data + Colors.ENDC)
    for key in self._data:
      if key != GameItemDataName.NAME:
        itemData = self._data[key]
        print('\t' + itemData.title + ': ', itemData.data)
