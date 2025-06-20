from turtle import Turtle
#Constant values:
MOVE_DISTANCE=20
EAST=0
NORTH=90
WEST=180
SOUTH=270

class Snake:
    #The constructor makes the start snake:
    def __init__(self):
        self.snake_parts=[]
        self.create_snake()
        self.head=self.snake_parts[0]

    #A function that makes a snake on call, by making a default snake with 3 body parts.
    def create_snake(self):
        snake_tail = Turtle()
        snake_body = Turtle()
        snake_head = Turtle()

        #Making a snake parts list, to easily keep track and modify the whole snake.
        self.snake_parts = [snake_head, snake_body, snake_tail]

        #go_left variable is set to decrement every part by 20 pixels to the left, so the snake doesnt overlap its other parts.
        go_left = 0
        #Initiating the snake parts:
        for snake in self.snake_parts:
            snake.shape("square")
            snake.color("green")
            snake.penup()
            snake.goto(go_left, 0)
            go_left -= 20

    #A function that keeps the whole snake moving 20 pixels in a loop on call:
    def move(self):
            # The below loop, updates each part location by the part ahead, so if the head part moves 10 y-axis, the rest of the parts move that way.
            for part in range(len(self.snake_parts) - 1, 0, -1):
                new_x = self.snake_parts[part - 1].xcor()
                new_y = self.snake_parts[part - 1].ycor()
                self.snake_parts[part].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)
            #If the snake body enters one of the borders, this if block makes it render in the opposite border, like the classic snake game.
            if self.head.xcor() > 280 :
                self.head.goto(-280,self.head.ycor())
            elif self.head.xcor() < -295:
                self.head.goto(280,self.head.ycor())
            elif self.head.ycor() > 280:
                self.head.goto(self.head.xcor(),-280)
            elif self.head.ycor() < -280:
                self.head.goto(self.head.xcor(),280)

    #The 4 functions below are set to change the snake direction on call, and they cant change to opposite directions, making the snake collide on itself.
    def up(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def down(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def right(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def left(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    #This function adds a tail part (object) to the snake on call.
    def add_tail(self):
        new_tail=Turtle()
        new_tail.shape("square")
        new_tail.color("green")
        new_tail.penup()
        new_tail.goto(self.snake_parts[-1].position())
        self.snake_parts.append(new_tail)

    #New function that basically resets the snake, and get the old snake outside of the screen view.
    def reset_snake(self):
        for part in self.snake_parts:
            part.goto(1000,1000)
        self.snake_parts.clear()
        self.create_snake()
        self.head=self.snake_parts[0]



