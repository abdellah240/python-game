from item import Item

class Menu:
  def __init__(self,title, items, background):
    self.title=title
    self.items=items
    self.background=background
        
  def display(self,width=40):
    print(f"{self.title.center(width,'*')}")
    print()
    
    def displayLayout(self):   
      match self.title:
        case "Main Menu":
          for i in self.items:
            i = str(i)
            print(f"{i}".center(width))
             
    displayLayout(self)                  
    print(f"{self.background.center(width)}")
    print("\n"+ "*"*width)    
