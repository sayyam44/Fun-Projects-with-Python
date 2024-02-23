from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__() #we have inherited the Turtle class as we can directly call the features of turtle class without using the keyword turtle
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5 , stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
        self.refresh()

    def refresh(self): #this will generate new food in case of collision
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
