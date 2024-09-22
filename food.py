import random
from  turtle import Turtle
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed(0)
        x = random.randint(-270, 270)
        y = random.randint(-280, 280)
        self.goto(x, y)
    def food_eaten(self):
        x = random.randint(-250, 250)
        y = random.randint(-270, 270)
        self.goto(x, y)