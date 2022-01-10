from turtle import Turtle


class Crosser(Turtle):
    def __init__(self):
        super().__init__()
        self.make_chris_cross()
        self.start_chris_cross()

    def make_chris_cross(self):
        self.shape('turtle')
        self.shapesize(stretch_wid=.6, stretch_len=.6)
        self.penup()
        
    def start_chris_cross(self):
        self.goto(0, -267)
        self.setheading(90)


    def forward(self):
        self.setheading(90)
        self.goto(self.xcor(), self.ycor() + 25)


    def backward(self):
        self.setheading(90)
        if self.ycor() <= -279:
            pass
        else:
            self.goto(self.xcor(), self.ycor() - 25)


    def left(self):
        self.setheading(180)
        if self.xcor()  <= -280:
            pass
        else:
            self.goto(self.xcor() - 15, self.ycor())

    def right(self):
        self.setheading(0)
        if self.xcor()  >= 280:
            pass
        else:
            self.goto(self.xcor() + 15, self.ycor())
        