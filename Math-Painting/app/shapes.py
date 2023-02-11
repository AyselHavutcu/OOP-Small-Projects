class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.color = color
        self.side = side

    def draw(self, canvas):
        """draws itself into canvas"""
        """from self.x to self.side is the rows and from self.y to self.side is for the columns"""
        canvas.data[self.x:self.x + self.side, self.y: self.y + self.side] = self.color


class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        """draws itself into canvas"""
        """from self.x to self.height is the rows and from self.y to self.width is for the columns"""
        canvas.data[self.x:self.x + self.height, self.y: self.y + self.width] = self.color