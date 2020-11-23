from src.TermColors import Colors, colorText
from src.ItemData import ItemData
from src.inputUtils import parseToInt, parseToFloat
import pprint

pp = pprint.PrettyPrinter(indent=2)
prettyFormat = pp.pformat


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
      parsedChoice = parseToInt(choice, 1, dataKeyList.__len__() + 1)

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
    elif(dataName == GameItemDataName.MARKET_SELL_PRICE):
      self.editMarketSellPricePrompt()
      return

    newValue = input('Enter a new value for "' +
                     self._data[dataName].title + '": ')
    self._data[dataName].data = newValue
    print('Value successfully changed')

  def editMarketSellPricePrompt(self):
    correctValueEntered = False
    while (correctValueEntered is False):
      newValue = input('Enter a new value for "' +
                       self._data[GameItemDataName.MARKET_SELL_PRICE].title + '": ')
      parsedValue = parseToFloat(newValue, min=0)
      if (parsedValue is not None):
        self._data[GameItemDataName.MARKET_SELL_PRICE].data = parsedValue
        correctValueEntered = True
    print('Value successfully changed')

  def editCraftingCostPrompt(self):
    doneEditing = False
    while(doneEditing is False):
      craftingItems = self._data[GameItemDataName.CRAFTING_COST].data
      print(colorText(prettyFormat(craftingItems), Colors.OKGREEN))
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
        self.addCraftingItemPrompt()
      elif (inputStr.startswith('delete')):
        self.deleteCraftingItem(inputStr[7:])
      elif (inputStr.startswith('edit')):
        self.editCraftingItemPrompt(inputStr[5:])

  def addCraftingItemPrompt(self):
    name = input('Enter the name of the crafting component: ')
    parsedChoice = None
    while (parsedChoice == None):
      quantity = input('Enter the quantity of the crafting component: ')
      parsedChoice = parseToInt(quantity, 1)
      if (parsedChoice is not None):
        craftingItems = self._data[GameItemDataName.CRAFTING_COST].data
        craftingItems[name] = parsedChoice
        self._data[GameItemDataName.CRAFTING_COST].data = craftingItems

  def editCraftingItemPrompt(self, craftItemName):
    selectionMade = False
    craftingDataItem = self._data[GameItemDataName.CRAFTING_COST]
    craftItemQuantity = craftingDataItem.data[craftItemName]
    while(selectionMade == False):
      print('Edit the name or the quantity?')
      print('name: ' + craftItemName)
      print('qty: ' + craftItemQuantity)
      selection = input('name, qty, or exit: ')
      if selection == 'exit':
        selectionMade = True
        return
      elif selection == 'qty':
        quantity = input('Enter the quantity of the crafting component: ')
        parsedQty = parseToInt(quantity, 1)
        if (parsedQty is not None):
          craftingItems = craftingDataItem.data
          craftingItems[craftItemName] = parsedQty
          craftingDataItem.data = craftingItems
          selectionMade = True
      elif selection == 'name':
        newName = input('Enter the new name of the crafting component: ')
        craftingItems = craftingDataItem.data
        craftingItems[newName] = craftingItems[craftItemName]
        del craftingItems[craftItemName]
        craftingDataItem.data = craftingItems
        selectionMade = True

  def deleteCraftingItem(self, craftItemName):
    craftingItems = self._data[GameItemDataName.CRAFTING_COST].data
    if (craftItemName in craftingItems):
      del craftingItems[craftItemName]
      self._data[GameItemDataName.CRAFTING_COST].data = craftingItems
    else:
      print('Crafting item with name: "' + craftItemName + '" does not exist' +
            ' for "' + self._data[GameItemDataName.NAME].data + '"')

  def print(self, gameItems):
    """Prints values for this game item to the console"""
    print(Colors.OKBLUE + self._data['name'].data + Colors.ENDC)
    for key in self._data:
      if key != GameItemDataName.NAME:
        itemData = self._data[key]
        itemValue = itemData.data
        itemTitle = itemData.title
        if type(itemValue) is float:
          itemValue = "{:,}".format(itemValue)
        elif type(itemValue) is dict:
          itemValue = str(prettyFormat(itemValue))
        print('\t' + itemTitle + ': ', colorText(itemValue, Colors.OKGREEN))
    craftItems = self._data[GameItemDataName.CRAFTING_COST].data
    totalMarketCost = 0
    allCraftItemsFound = True
    for craftItemName, craftItemQty in craftItems.items():
      craftItemObj = gameItems.getItem(craftItemName)
      if (craftItemObj is not None):
        craftItemMarketCost = craftItemObj.getData(GameItemDataName.MARKET_SELL_PRICE).data
        if (craftItemMarketCost is not None):
          totalMarketCost += craftItemMarketCost * craftItemQty
        else:
          allCraftItemsFound = False
      else:
        allCraftItemsFound = False
    if (allCraftItemsFound):
      print('\tCraft item total market cost: ' + "{:,}".format(totalMarketCost))
    else:
      print('\tCraft item total market cost: ' + 'unknown because some ' +
            'crafting items do not have a market value')
