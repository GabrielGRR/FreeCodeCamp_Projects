""" 
Fourth exercise from FreeCodeCamp https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator
 """

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width
        return width

    def set_height(self, height):
        self.height = height
        return height

    def get_area(self):
        area = self.width*self.height
        return area
    
    def get_perimeter(self):
        perimeter = self.width*2 + self.height*2
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width**2 + self.height**2)**.5
        return diagonal

    def get_picture(self):
        lines = 0
        if self.width >50 or self.height >50:
            return "Too big for picture."
        else:
            picture = ""    
            while lines < self.height:
                picture+="*"*self.width + '\n'
                
                lines+=1
            return picture

    def get_amount_inside(self,obj):
        qtt_shapes_inside = self.width//obj.width * self.height//obj.height
        return qtt_shapes_inside

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.height = side
        self.width = side

    def __str__(self):
        return f"Square(side={self.side})"

    def set_side(self, side):
        self.side = side
        self.height = side
        self.width = side

    def set_width(self, side):
        self.side = side
        self.height = side
        self.width = side

    def set_width(self, side):
        self.side = side
        self.height = side
        self.width = side

""" 

rect = Rectangle(5, 5)
print(rect.get_area())
rect.set_width(3)
print(rect.get_picture())
print(rect.get_perimeter())
print(rect)

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_picture())
print(sq.get_diagonal())
print(sq) 
"""