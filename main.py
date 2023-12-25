import time
from turtle import Turtle, Screen
from snake import Snake


hello = "My Snake Game"




screen = Screen()
screen.bgcolor('black')
screen.tracer(0)
screen.title(hello)

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

##Create a snake body

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()



## Move the snake














screen.exitonclick()