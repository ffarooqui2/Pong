from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_player_score = 0
        self.r_player_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 300)
        self.write(self.l_player_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 300)
        self.write(self.r_player_score, align="center", font=("Courier", 80, "normal"))

    def left_player_scores(self):
        self.l_player_score += 1
        self.update_scoreboard()

    def right_player_scores(self):
        self.r_player_score += 1
        self.update_scoreboard()

