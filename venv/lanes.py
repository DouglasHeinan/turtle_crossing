from turtle import Turtle

class Lanes(Turtle):
    def __init__(self):
        super().__init__()
        self.make_lanes()

    def make_lanes(self):
        self.hideturtle()
        self.penup()
        self.setheading(180)
        self.goto(300, 250)
        for lane in range(22):
            self.pendown()
            self.forward(600)
            self.penup()
            self.goto(300, 250 - (25 * lane))