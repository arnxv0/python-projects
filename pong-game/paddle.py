from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, initial_position):
        super().__init__()
        self.initial_position = initial_position
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(initial_position)

    def move_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if -240 < self.ycor():
            self.goto(self.xcor(), self.ycor() - 20)
