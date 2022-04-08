from turtle import Turtle, Screen
import random


def move_fowards():
    user_turtle.forward(10)


def move_backwards():
    user_turtle.backward(10)


def move_right():
    user_turtle.rt(90)
    user_turtle.forward(20)
    user_turtle.lt(90)


def move_left():
    user_turtle.lt(90)
    user_turtle.forward(20)
    user_turtle.rt(90)


def collision_det(user_turtle, enemy_turtle):
    return abs(user_turtle.pos() - enemy_turtle.pos()) < 15


def game_state(won):
    pen = Turtle()
    pen.hideturtle()
    pen.pu()
    pen.goto(-180, 0)
    if not won:
        pen.color("red")
        pen.write("Game Over", move=False, font=('Arial', 40, 'normal'))
    else:
        pen.color("blue")
        pen.write("You won", move=False, font=('Arial', 40, 'normal'))


continue_game = True
won = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["black", "red", "grey", "red", "grey", "black"]
all_turtle = []
incr_y = -40
incr_x = 0

# Creates the finish line
finish_line = Turtle()
finish_line.color("blue")
finish_line.pu()
finish_line.goto(x=240, y=-190)
finish_line.pd()
finish_line.pensize(50)
finish_line.lt(90)
finish_line.forward(400)
# creates user turtle
user_turtle = Turtle(shape="turtle")
user_turtle.color("green")
user_turtle.pu()
user_turtle.goto(x=-250, y=-30)

# create enemy turtles
for color_str in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_str)
    new_turtle.pu()
    rand_pos = random.randint(1, 50)
    if rand_pos % 2:
        y_pos = -100
    else:
        y_pos = 50
    new_turtle.goto(x=-120 + incr_x, y=y_pos)
    incr_x += 60
    new_turtle.lt(90)
    all_turtle.append(new_turtle)

while continue_game:
    # control the user turtle
    screen.listen()
    screen.onkey(key="Right", fun=move_fowards)
    screen.onkey(key="Left", fun=move_backwards)
    screen.onkey(key="Up", fun=move_left)
    screen.onkey(key="Down", fun=move_right)
    for turtle in all_turtle:
        # enemy_turtles goes in reverse
        if turtle.ycor() > 50 or turtle.ycor() < -100:
            turtle.left(90)
            turtle.forward(20)
        # detects if the turtle hits another turtle
        if collision_det(user_turtle, turtle):
            continue_game = False
            won = False
        # detects when the turtle made it to the water
        if user_turtle.xcor() == 220:
            continue_game = False
            won = True
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

game_state(won)
screen.exitonclick()
