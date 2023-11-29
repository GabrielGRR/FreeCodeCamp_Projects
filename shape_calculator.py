class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

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

    def set_side(self, side):
        self.side = side