from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20 #these are few variables that we are defining initially because if there will be any change then directly we can cange the values from here we need not to go through the code.

UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0] #since we will use the head very frequently so directly saving the head in variable head

    def create_snake(self):
        # creating the snake body by breaking it into 3 segments
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            # new_segment = Turtle("square")
            # new_segment.color("white")
            # new_segment.penup()  # as the segments move there will be no line behind
            # new_segment.goto(position)
            # self.segments.append(new_segment)  # head->middle->end

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()  # as the segments move there will be no line behind
        new_segment.goto(position)
        self.segments.append(new_segment)  # head->middle->end

    def extend(self):
        #add new segment to the snake
        self.add_segment(self.segments[-1].position()) #getting the hold of the last segment of the list

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)  # moving the last(end)segment to move to the position of second last segment
        self.head.forward(MOVE_DISTANCE)  # moving all the segments forward
        # segments[0].left(90) #moving the 1st segment left

    def up(self):
        if self.head.heading() != DOWN: #if the head is moving downwards then the head cannot move upwards as it will become backwards
            self.head.setheading(UP)
            # self.head.setheading(90)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            # self.head.setheading(270)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            # self.head.setheading(180)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            # self.head.setheading(0)