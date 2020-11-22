class GameItem:
  """Represents an item in the game. Holds values for it's market value and
  sub-components"""

  def __init__(self, name):
    self.name = name

  def printItem(self):
    """Prints values for this game item to the console"""
    print(self.name)
