#we are gonna create the main the classes
#Import the required Libraries

""""UI part """
from canvas import  Canvas
from shapes import Rectangle,Square
import enum


"""enter values for canvas"""
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))
canvas_color = str(input("Enter canvas color black/white ? "))

canvas_color = (255,255,255) if canvas_color == 'white' else (0,0,0)

shape_canvas = Canvas(canvas_width,canvas_height,canvas_color)
"""create an enum class for colors """

class Colors(enum.Enum):
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    yellow = (255,255,0)
    green = (0,0,255)


def draw_rectangle(canvas):
    rec_x = int(input("Enter the rectangle's x point: "))
    rec_y = int(input("Enter the rectangle's y point: "))
    rec_width = int(input("Enter the rectangle's width: "))
    rec_height = int(input("Enter the rectangle's height: "))
    rec_color = str(input("Enter rectangle color:"))

    if rec_color.lower() == Colors[rec_color.lower()].name:
        rec_color = Colors[rec_color.lower()].value
    else:
        rec_color = str(input(f"Please enter a color in this list:".format([color.name for color in Colors])))
    rec = Rectangle(rec_x, rec_y, rec_width, rec_height, rec_color)
    rec.draw(shape_canvas)


def draw_square(canvas):
    square_x = int(input("Enter the square's x point: "))
    square_y = int(input("Enter the square's y point: "))
    square_side = int(input("Enter the square's side value: "))
    square_color = str(input("Enter rectangle color:"))

    if square_color.lower() == Colors[square_color.lower()].name:
        square_color = Colors[square_color.lower()].value
    else:
        square_color = str(input(f"Please enter a color in this list:".format([color.name for color in Colors])))

    square = Square(square_x, square_y, square_side, square_color)
    square.draw(shape_canvas)


while True:
      shape_type = str(input("Please Enter what you want to draw a rectangle or square ? Enter quit to quit."))

      if shape_type.lower() == 'rectangle':
          draw_rectangle(shape_canvas)

      elif shape_type.lower() == 'square':
         draw_square(shape_canvas)

      else:
          break


shape_canvas.make("canvas.png")





