# A class all about the snake
from turtle import Turtle

x_cord = 0
y_cord = 0
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # create three body segments of the snake
        for position in range(0, 2):
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        # prevents the turtle from drawing a line
        new_segment.penup()
        # set the color
        new_segment.color("green")
        # assign the segment to a certain coordinate
        global x_cord
        global y_cord
        new_segment.goto(x_cord, y_cord)
        self.segments.append(new_segment)
        x_cord -= 20

    def extend_segment(self, position):
        new_segment = Turtle(shape="square")
        # prevents the turtle from drawing a line
        new_segment.penup()
        # set the color
        new_segment.color("green")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        self.extend_segment(self.segments[-1].position())

    def move(self):

        # Get the third segment to move towards the second segment's position, same applies for
        # segment two to segment one
        # User only controls the movement of segment one, two other segment will just follow segment one
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

# Functions to set the direction of the snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
