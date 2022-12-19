from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from playboard import PlayBoard

screen = Screen()
screen.title("PONG")
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.tracer(0)  # Turns off animation

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

ball = Ball()
scoreboard = ScoreBoard()
playing_field = PlayBoard()

game_is_live = True

# default settings
ball_speed = 1
x_multiplier = -1
y_multiplier = -1

while game_is_live:
    ball.move(ball_speed, x_multiplier, y_multiplier)

    # Detect if right paddle misses ball
    if ball.xcor() >= 370:
        print(f"Game Ended")
        ball.goto(0, 0)
        ball_speed = 1
        x_multiplier = x_multiplier * -1
        y_multiplier = y_multiplier * -1
        scoreboard.left_player_scores()

    # Detect if left paddle misses ball
    if ball.xcor() <= -370:
        print(f"Game Ended")
        ball.goto(0, 0)
        ball_speed = 1
        x_multiplier = x_multiplier * -1
        y_multiplier = y_multiplier * -1
        scoreboard.right_player_scores()

    # Detect collision with top and bottom walls
    if ball.ycor() <= -280:
        y_multiplier = 1
    if ball.ycor() >= 280:
        y_multiplier = -1

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and 330 < ball.xcor() < 370:
        print(f"Made contact")
        x_multiplier = -1
        ball_speed += 0.5

    if ball.distance(left_paddle) < 50 and -330 > ball.xcor() > -370:
        print(f"Made contact")
        x_multiplier = 1
        ball_speed += 0.5

    screen.update()

screen.exitonclick()
