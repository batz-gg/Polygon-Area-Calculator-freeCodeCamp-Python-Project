class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
  
  def set_width(self, width):
    self.width = width
  
  def set_height(self, height):
    self.height = height

  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height
    return perimeter

  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return diagonal

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return  "Too big for picture."
    else:
      line = "*" * self.width + "\n"
      picture = line * self.height
      return picture

  def get_amount_inside(self, shape):
    import math
    if self.width < shape.width or self.height < shape.height:
      return 0
    else:
      amount = math.floor(self.width / shape.width) * math.floor(self.height / shape.height)
      return amount
      


class Square(Rectangle):
  def __init__(self, side):
    super().__init__(self, side)
    self.side = side
    self.width = side
    self.height = side

  def __str__(self):
    return f"Square(side={self.side})"
  
  def set_side(self, side):
    self.side = side
    self.width = side
    self.height = side
  
  def set_width(self, side):
    self.side = side
    self.width = side
    self.height = side
  
  def set_height(self, side):
    self.side = side
    self.width = side
    self.height = side