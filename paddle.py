from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        # Now every instance created using the Paddle class will get all the
        # functionality of that from the Turtle class
        self.shape("square")
        self.color("white")
        # Since turtle starts off at 20 x 20 pxl, we need to stretch it by multiplies those numbers to get 20 x 100
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto(coordinates)
        self.setheading(90)

    # Paddle Movement
    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
