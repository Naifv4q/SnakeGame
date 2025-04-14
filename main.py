from turtle import Screen
from time import sleep
from snake import  Snake
from food import Food
from scoreboard import ScoreBoard

#The screen of the program is initiated here with the below attributes
my_screen=Screen()
my_screen.setup(width=600,height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")

#Here the screen stopped updating, so it can only be updated when the snake is moving, the updating part happens in line 34 and below
#The reason behind this, is so the snake can move smoothly part by part, without delay, making a gap in the snake body.
my_screen.tracer(0)
my_screen.listen()
my_scoreboard = ScoreBoard()
snake = Snake()

#Below the snake movement control are set:
my_screen.onkey(fun=snake.up, key="Up")
my_screen.onkey(fun=snake.down,key="Down")
my_screen.onkey(fun=snake.right, key="Right")
my_screen.onkey(fun=snake.left, key="Left")

#Initiating a food object, that renders randomly withing the screen borders set in line 8
my_food = Food()
keep_going=True

while keep_going:
    #Here the screen updates, so the snake body doesn't have gaps, and only updates when they are set together
    my_screen.update()
    #A sleep function is set to make the game pace good enough to be playable, because without it, it will be too fast to be playable.
    sleep(0.1)
    snake.move()

    #Snake body Collision detection loop, if any part except the head using slicing, is close by 10 pixels to another part,
    #the program ends the game for collision with snake body and show a game over message
    for part in snake.snake_parts[1:]:
        if snake.head.distance(part) < 10:
            keep_going=False

    #Food collision detection loop, if the snake body is close by the food by its size (which is at start is 20 pixels) and adds a 10 more pixels as a buffer,
    #making it collide with the snake if it only hits the food by it's edge and not head on.
    #If it hits, a new food is spawned in a random location in the screen, and a new tail is added to the snake, lastly a score is added for the food taken.
    for part in snake.snake_parts:
        if part.distance(my_food) < my_food.full_size+10:
            my_food.new_food()
            snake.add_tail()
            my_scoreboard.add_score()    




#The below screen function keeps the screen on display until closed by user
my_screen.mainloop()
