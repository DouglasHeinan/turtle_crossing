from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self, start_y_dict, start_list, level):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=.6, stretch_len=.9)
        color_list = ['blue', 'black', 'red', 'green', 'orange', 'yellow']
        self.color(random.choice(color_list))
        self.goto(random.choice(start_list))
        self.speed = start_y_dict[self.ycor()] + level
        if self.xcor() == 300:
            self.setheading(180)
        else:
            self.setheading(0)
        self.showturtle()
        
    def start_car(self):
        self.goto(random.randrange(-280, 281), self.ycor())

        
    def drive(self):
        self.forward(self.speed)





