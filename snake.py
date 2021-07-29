from turtle import Turtle

move_distance = 20
up = 90
down = 270
right = 0
left = 180
position = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for x in position:
            self.add_snake(x)

    def add_snake(self, position):
        new_turtle = Turtle("turtle")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.snake.append(new_turtle)


    def extend(self):
        #add new snake
        self.add_snake(self.snake[-1].position())

    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(move_distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
