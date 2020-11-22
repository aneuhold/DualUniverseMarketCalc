from src.TermColors import Colors


class GameItem:
  """Represents an item in the game. Holds values for it's market value and
  sub-components"""

  def __init__(self, name):
    self._name = name
    self._marketSellPrice = None
    self._craftingCost = {}

  def getMarketSellPrice(self):
    return self._marketSellPrice

  def setMarketSellPrice(self, newVal):
    self._marketSellPrice = newVal

  marketSellPrice = property(getMarketSellPrice, setMarketSellPrice,
                             doc="The market sell price of this game item")

  def addCraftingCost(self, itemName, quantity):
    self._craftingCost[itemName] = quantity

  def print(self):
    """Prints values for this game item to the console"""
    print(Colors.OKBLUE + self._name + Colors.ENDC)
    print('\tMarket Sell Price: ', self._marketSellPrice)
    print('\tCrafting Cost: ', self._craftingCost)
