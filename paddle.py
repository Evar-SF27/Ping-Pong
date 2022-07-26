from turtle import Turtle
import random

player_colors = ["grey", "white", "red", "black", "pink"]


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color(random.choice(player_colors))
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        if self.ycor() < 220:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if self.ycor() > -220:
            self.goto(self.xcor(), new_y)