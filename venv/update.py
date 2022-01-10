from turtle import Turtle
import time
'''
A file to be imported into the turtle_crossing file
'''

ALIGNMENT = 'center'
FONT = 'Ariel'

class Update(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        
    def stage_start(self, level, lives):
        self.goto(0, 50)
        self.write(arg=f"Level {level}", align=ALIGNMENT, font=FONT)
        self.goto(0, -50)
        self.write(arg=f"Lives remaining: {lives}", align=ALIGNMENT, font=FONT)
        time.sleep(3)
        self.clear()
        
    def game_over(self, level):
        self.goto(0, 50)
        self.write(arg="Game Over", align=ALIGNMENT, font=FONT)
        self.goto(0, -50)
        self.write(arg=f"{level} levels completed", align=ALIGNMENT, font=FONT)
        
    def new_level(self, level):
        self.goto(0, 50)
        self.write(arg="Congratulations", align=ALIGNMENT, font=FONT)
        self.goto(0, -50)
        self.write(arg=f"You've advanced to level {level}", align=ALIGNMENT, font=FONT)
        time.sleep(3)
        self.clear()


        

