from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('pink')
        self.shape('circle')
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        # self.setheading(random.randint(45, 160))
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        #Speed up ball after every paddle bounce

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_paddle()
