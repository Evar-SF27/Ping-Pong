import time
import random
from math import dist as d
from turtle import Screen
from draw import Draw
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

field_colors = ["blue", "orange", "green"]

# Setting up the screen
screen = Screen()
screen.bgcolor(random.choice(field_colors))
screen.setup(width=1300, height=700)
screen.title("Ping Pong")
screen.tracer(0)

# Drawing the field lines
draw = Draw()

# Setting up paddle
left_paddle = Paddle((-565, 0))
right_paddle = Paddle((560, 0))

# Setting up ball
ball = Ball()

# Setting up scoreboard
scoreboard = Scoreboard()

# Key event listeners
screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.02)
    screen.update()
    ball.move()

    # Detecting collision with the walls
    if ball.ycor() > 272 or ball.ycor() < -277:
        ball.bounce()

    # Detecting collision with the paddle
    ball_cor = [ball.xcor(), ball.ycor()]
    left_pad_cor = [left_paddle.xcor(), left_paddle.ycor()]
    right_pad_cor = [right_paddle.xcor(), right_paddle.ycor()]
    left_dist = d(ball_cor, left_pad_cor)
    right_dist = d(ball_cor, right_pad_cor)

    if left_dist < 60 and ball.xcor() < -535 or right_dist < 60 and ball.xcor() > 525:
        ball.hit()

    # Detecting breaking of bounce
    if ball.xcor() > 580:
        scoreboard.update_l_score()
        ball.reset()
    if ball.xcor() < -580:
        scoreboard.update_r_score()
        ball.reset()

    # End the game
    player1_score = scoreboard.l_score
    player2_score = scoreboard.r_score

    if player1_score == 12:
        scoreboard.show_score()
        game_is_on = False
        
    if player2_score == 12:
        scoreboard.show_score()
        game_is_on = False
    
    if player1_score - player2_score >= 5 or player2_score - player1_score >= 5:
        scoreboard.show_score()
        game_is_on = False

screen.exitonclick()
