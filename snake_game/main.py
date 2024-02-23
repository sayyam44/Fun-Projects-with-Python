from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# starting_position = [(0,0),(-20,0),(-40,0)] #defining the starting position for all the 3 segments
snake = Snake() #step 1- create snake function will be triggered from snake.py
# segments=[]
food=Food()
scoreboard = Scoreboard()

# #creating the snake body by breaking it into 3 segments
# for position in starting_position:
#     new_segment=Turtle("square")
#     new_segment.color("white")
#     new_segment.penup() #as the segments move there will be no line behind
#     new_segment.goto(position)
#     segments.append(new_segment)#head->middle->end
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on= True
while game_is_on:
    screen.update() #refresh the screen
    time.sleep(0.1) #delay for 0.1 sec
    # for seg in segments:
    #     seg.forward(20)
        # screen.update()  # so that all the 3 segments move together
        # time.sleep(1)  # it adds 1 sec delay after each segment moves
    snake.move() #step 2 :- moving the snake

    #detect collision with the food
    if snake.head.distance(food) < 15: #as the food size is 10*10
        # print("nooooooooooooo")
        food.refresh() #in order to move snake to a new position after collision
        snake.extend()
        scoreboard.increase_score()


    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor() <-280: #all the cases if the snake hits the wall
        game_is_on = False
        scoreboard.game_over()

    #detect collision with tail
    # if head collides with any segment in the tail:
    # trigger game_over
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
    # for seg_num in range(len(segments)-1,0,-1):
    #     new_x=segments[seg_num-1].xcor()
    #     new_y=segments[seg_num-1].ycor()
    #     segments[seg_num].goto(new_x,new_y) #moving the last(end)segment to move to the position of second last segment
    # segments[0].forward(20) #moving all the segments forward
    # segments[0].left(90) #moving the 1st segment left


# segment_1=Turtle("square")
# segment_1.color("white")
#
# segment_2=Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20,0)
#
# segment_3=Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40,0)



screen.exitonclick()
