from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: int
    discount: float
    category: str
    img:str
    def __init__(self,name,price,discount,category,img):
      self.name=name
      self.price=price
      self.discount=discount
      self.category=category
      self.img=img



