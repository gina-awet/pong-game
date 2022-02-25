from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

# Screen setup
screen = Screen()
screen.screensize(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# Create paddle & ball objects and assign paddle keys
paddle_right = Paddle()
paddle_right.goto(350, 0)
paddle_left = Paddle()
paddle_left.goto(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_right.go_up, 'Up')
screen.onkey(paddle_right.go_down, 'Down')
screen.onkey(paddle_left.go_up, 'w')
screen.onkey(paddle_left.go_down, 's')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_wall()

    #Detect collision with paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    #Right Player misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        scoreboard.update()
        ball.reset()

    #Left Player misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        scoreboard.update()
        ball.reset()


screen.exitonclick()