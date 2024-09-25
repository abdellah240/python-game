# abstract class > clickableItem | non-clickable item
from abc import *

class Item(ABC): 
    
  @abstractmethod
  def setBorder(self):
    pass

    def __init__(self,displayedElement):
      self.displayedElement=displayedElement
      self.border=None

class clickableItem(Item):
  def __init__(self, displayedElement, link):
    super().__init__(displayedElement)
    self.link=link
    self.setBorder()

  def setBorder(self):
    self.border="-" 
