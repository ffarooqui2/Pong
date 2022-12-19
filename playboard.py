from turtle import Turtle


class PlayBoard(Turtle):

    def __init__(self):

        super().__init__()
        self.goto(400, 300)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.pendown()

        for walls in range(0, 2):
            self.right(90)
            self.forward(600)
            self.right(90)
            self.forward(800)
