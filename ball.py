from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self, speed, x_multiplier, y_multiplier):
        self.goto(self.xcor() + (speed * x_multiplier), self.ycor() + (speed * y_multiplier))

