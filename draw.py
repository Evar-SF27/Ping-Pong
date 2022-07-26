from turtle import Turtle


class Draw(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.pensize(3)
        self.penup()
        self.draw_mid()
        self.draw_side_line()
        self.draw_back_line()
        self.draw_inner_side_line()
        self.draw_inner_line()

    def draw_mid(self):
        self.goto(0, 300)
        self.pendown()
        self.goto(0, -300)
        self.penup()

    def draw_side_line(self):
        self.goto(-590, 300)
        self.pendown()
        self.goto(590, 300)
        self.penup()
        self.goto(-590, -300)
        self.pendown()
        self.goto(590, -300)
        self.penup()

    def draw_back_line(self):
        self.goto(-592, 300)
        self.pendown()
        self.goto(-592, -300)
        self.penup()
        self.goto(590, 300)
        self.pendown()
        self.goto(590, -300)
        self.penup()

    def draw_inner_side_line(self):
        self.goto(-590, 210)
        self.pendown()
        self.goto(590, 210)
        self.penup()
        self.goto(-590, -210)
        self.pendown()
        self.goto(590, -210)
        self.penup()

    def draw_inner_line(self):
        self.goto(-432, 210)
        self.pendown()
        self.goto(-432, -210)
        self.penup()
        self.goto(430, 210)
        self.pendown()
        self.goto(430, -210)
        self.penup()
