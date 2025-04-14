from turtle import Turtle
from random import randint
class Food(Turtle):
    def __init__(self):
        super().__init__()
        #Inherting the turtle class, to make a 'turtle' food object for the snake to progress.
        #Its shape set to 'circle'.
        self.shape("circle")
        #Raising the pen of the object so it doesn't draw on the screen.
        self.penup()
        #Initiaitng a full size variable, because the food size changes every time its eaten.
        self.full_size=0
        #Setting the default start size of the food to 20 by 20 pixels.
        self.shapesize(stretch_wid=1,stretch_len=1)
        #setting and initiating the default wide and len stretch values of the food object.
        self.new_wide_stretch = 1
        self.new_len_stretch = 1
        #setting the food object color to orange
        self.color("orange")
        #A function new_food is called to spawn one
        self.new_food()
    #A function that makes a new food object when called.
    def new_food(self):
        self.shapesize(stretch_wid=self.new_wide_stretch,stretch_len=self.new_len_stretch)
        self.new_wide_stretch-=0.05
        self.new_len_stretch-=0.05

        #Rounding the new stretch values, to 2 decimals after the point.
        self.new_len_stretch=round(self.new_len_stretch,2)
        self.new_wide_stretch=round(self.new_wide_stretch,2)

        #Setting the full_size variable to the new food size
        self.full_size=(self.new_wide_stretch + self.new_len_stretch)*10

        #This if block  checks if the food is going below 0.1, if so it resets the food size to 1.0, meaning 20 by 20 pixels
        if self.new_len_stretch <=0.10:
            self.new_len_stretch=1
            self.new_wide_stretch=1
        
        #Random x and y values based on the screen height and width.
        random_x = randint(-290, 290)
        random_y = randint(-290, 290)
        self.goto(random_x, random_y)
    #Object that resets the food object when called.
    def reset_food(self):
        self.shapesize(stretch_wid=1,stretch_len=1)

