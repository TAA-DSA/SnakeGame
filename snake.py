from turtle import Turtle

coordinates = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
Up = 90
Down = 270
Left = 180
Right = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # create snake
        for cor in coordinates:
            self.add_segment(cor)

    def add_segment(self, position):
        snake = Turtle(shape='square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    # move snake
    def move(self):
        for snakes_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snakes_num - 1].xcor()
            new_y = self.segments[snakes_num - 1].ycor()
            self.segments[snakes_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)

    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)
