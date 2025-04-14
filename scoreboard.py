from turtle import Turtle
from time import sleep
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        #Inherting the turtle class, to make a 'turtle' tile for the score, then setting its attributes as seen below:
        #Here we hide the turtle that comes from initiating the turtle object.
        self.ht()
        #Here we raise the pen so the object doesn't draw in the screen.
        self.penup()
        #Making the score font white.
        self.color("White")
        #Setting the score location in the up right corner of the screen.
        self.goto(-255,275)
        #initaiting a score variable.
        self.score=0
        #Writing the score on the screen using the write() function.
        self.write(f"Score: {self.score}", False,"Center",("Arial",15,"normal"))
    #Simply adds +1 to the score counter when called, and clearing the previous score and updating it with the new one.
    def add_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}", True,"Center",("Arial",15,"normal"))
        self.goto(-255,275)
    #A game over message shows when called.
    def show_game_over(self):
        self.game_over = Turtle()
        self.game_over.ht()
        self.game_over.penup()
        self.game_over.goto(0,0)
        self.game_over.color("red")
        self.game_over.write("GAME OVER !",False,"Center",("Arial",15,"normal"))
        
    


