from canvas import Canvas
from shapes import Rectangle, Square


def rectangle_inputs(canvas):
    rect = Rectangle(int(input("Enter X coordinate: ")), int(input("Enter Y coordinate: ")),
                     int(input("Enter the rectangle width: ")), int(input("Enter the rectangle height: ")),
                     list(map(int, input("Enter the rectangle color: ").strip("[]").split(","))))
    rect.draw(canvas)


def square_inputs(canvas):
    squa = Square(int(input("Enter X coordinate: ")), int(input("Enter Y coordinate: ")),
                  int(input("Enter the square side: ")),
                  list(map(int, input("Enter the rectangle color: ").strip("[]").split(","))))
    squa.draw(canvas)


def main():
    canvas = Canvas(int(input("Enter the canvas width: ")), int(input("Enter the canvas height: ")),
                    list(map(int, input("Enter the canvas color: ").strip(' []').split(','))))
    while True:
        shape_input = input("What would u like to draw? (Rectangle or square)\nEnter quit to quit. ").lower()
        if shape_input == "rectangle":
            rectangle_inputs(canvas)
        elif shape_input == "square":
            square_inputs(canvas)
        elif shape_input == "quit":
            break

    canvas.make()


if __name__ == "__main__":
    main()
