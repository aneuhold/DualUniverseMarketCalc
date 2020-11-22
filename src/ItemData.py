class ItemData:
  def __init__(self, title, data):
    self._title = title
    self._data = data

  def getTitle(self):
    return self._title

  def setTitle(self, newTitle):
    self._title = newTitle

  title = property(getTitle, setTitle)

  def getData(self):
    return self._data

  def setData(self, newData):
    self._data = newData

  data = property(getData, setData)
