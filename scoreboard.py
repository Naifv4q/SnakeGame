from turtle import Turtle
from time import sleep
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        #Inherting the turtle class, to make a 'turtle' tile for the score, then setting its attributes as seen below:

        #Here we hide the turtle that comes from initiating the turtle object.
        self.ht()

        #Adding a high score to the game, to keep track of the highest score the user ever got.
        self.high_score= self.read_high_score()

        #Here we raise the pen so the object doesn't draw in the screen.
        self.penup()

        #Making the score font white.
        self.color("White")

        #Setting the score location in the upper center of the screen.
        self.goto(0,275)

        self.score=0
        #Writing the score on the screen using the write() function.
        self.write(f"Score: {self.score}  High Score: {self.high_score}", True,"Center",("Arial",15,"normal"))

    #This method simply updates the score on the screen.
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", True,"Center",("Arial",15,"normal"))
        self.goto(0,275)

    #A score reset, when the player loses the previous game.
    def score_reset(self):
        if self.score > self.high_score:
            self.write_high_score(self.score)
            self.high_score = self.read_high_score()
        self.score=0
        self.update_score()
    
    #A function that adds a new score on call.
    def add_score(self):
        self.score+=1
        self.clear()
        self.update_score()

    #A function that reads the highest score in the score_memory.txt file.
    def read_high_score(self):
        with open("score_memory.txt",mode="r") as memory_file:
            return int(memory_file.read())
        

    #A function that writes the highest score the user gets in the score_memory.txt file.
    def write_high_score(self,score):
        with open("score_memory.txt",mode="w") as memory_file:
            memory_file.write(f"{score}")


    #Below is an old code, I kept it for documentation.

    #A game over message shows when called.
    #
    # def show_game_over(self):
    #     self.game_over = Turtle()
    #     self.game_over.ht()
    #     self.game_over.penup()
    #     self.game_over.goto(0,0)
    #     self.game_over.color("red")
    #     self.game_over.write("GAME OVER !",False,"Center",("Arial",15,"normal"))
        
    


