from turtle import *
import time
import random

colors = ["red", "orange", "yellow", "green", "blue"]
x_coord = -450
y_coord = 220
all_blocks = []
game = False
x_move = 20
y_move = 20
move_speed = 0
score = 000
game_on = False
last_player_move_time = time.time()


def start_game():
    global x_move, y_move, score, game_on, x_coord, y_coord
    global start_instruction
    display.onkeypress(None, "space")
    x_move = 10
    y_move = 10
    display.tracer(False)
    start_instruction.reset()
    start_instruction.penup()
    start_instruction.goto(-1000, -1000)
    game_on = True
    ball.goto(player.xcor() + 50, player.ycor())
    display.tracer(True)
    while game_on:
        if len(all_blocks) == 0:
            x_coord = -450
            y_coord = 220
            generate_blocks()
        time.sleep(move_speed)
        move_ball()
        if ball.xcor() > 469 or ball.xcor() < -469:
            bounce()

        if ball.distance(player) <= 80 and ball.ycor() <= -250:
            hit()

        if ball.ycor() >= 440:
            hitblocks()

        if ball.ycor() < -281:
            game_on = False
            display.tracer(False)
            start_instruction.goto(0, 50)
            start_instruction.color("white")
            start_instruction.write("Game Over\nPress Space to restart", align="center", font=("Fixedsys", 35, "bold"))
            display.onkeypress(start_game, "space")
            score = 0
            for block in all_blocks:
                block.goto(-1000, -1000)
            x_coord = -450
            y_coord = 220
            score = 0
            scoreboard.clear()
            scoreboard.write(f"SCORE\n {score}", align="center", font=("Fixedsys", 70, "bold"))
            generate_blocks()
            player.goto(0, -280)

        if game_on:
            for i in all_blocks:
                if ball.distance(i) < 40:
                    display.tracer(False)
                    i.hideturtle()
                    hitblocks()
                    all_blocks.remove(i)
                    i.goto(-1000, 1000)
                    score += 1
                    scoreboard.clear()
                    scoreboard.write(f"SCORE\n {score}", align="center", font=("Fixedsys", 70, "bold"))
                    display.tracer(True)

def draw_outline():
    display.tracer(False)
    border_left = Turtle()
    border_left.color("white")
    border_left.hideturtle()
    border_left.penup()
    border_left.goto(-480, -285)
    border_left.pendown()
    border_left.setheading(90)
    border_left.forward(900)

    border_right = Turtle()
    border_right.color("white")
    border_right.hideturtle()
    border_right.penup()
    border_right.goto(480, -285)
    border_right.pendown()
    border_right.setheading(90)
    border_right.forward(900)

    border_bottom = Turtle()
    border_bottom.color("white")
    border_bottom.hideturtle()
    border_bottom.penup()
    border_bottom.goto(-480, -285)
    border_bottom.pendown()
    border_bottom.forward(960)
    display.tracer(True)

    exit_instruction = Turtle()
    exit_instruction.color("white")
    exit_instruction.hideturtle()
    exit_instruction.penup()
    exit_instruction.goto(0, -390)
    exit_instruction.pendown()
    exit_instruction.write(">>>>> Click Esc to exit <<<<<", align="center", font=("Fixedsys", 10, "bold"))


def bounce():
    global x_move
    x_move *= -1


def hit():
    global y_move, move_speed, x_move
    if ball.xcor() >= player.xcor():
        x_move = 10
    else:
        x_move = -10
    y_move *= -1


def hitblocks():
    global y_move
    y_move *= -1


def move_ball():
    global x_move, y_move
    new_x = ball.xcor() + x_move
    new_y = ball.ycor() + y_move
    ball.goto(new_x, new_y)


def generate_blocks():
    display.tracer(False)
    global x_coord, y_coord
    for i in range(64):
        color = colors[random.randint(0, len(colors) - 1)]
        block = Turtle("square")
        block.speed(10)
        block.color(color)
        block.turtlesize(2, 3, 1)
        block.penup()
        block.hideturtle()
        block.goto(x_coord, y_coord)
        block.showturtle()
        x_coord += 60
        print(x_coord)
        if x_coord > 450:
            y_coord += 41
            x_coord = -450
        all_blocks.append(block)
    display.tracer(True)

def move_left():
    global last_player_move_time
    current_time = time.time()
    if current_time - last_player_move_time >= 0.1 and 400 >= player.xcor() > - 400:
        player.backward(40)
        last_player_move_time = current_time

def move_right():
    global last_player_move_time
    current_time = time.time()
    if current_time - last_player_move_time >= 0.1 and 400 > player.xcor() >= - 400:
        player.forward(40)
        last_player_move_time = current_time

display = Screen()
display.screensize(900, 300, "black")
display.getcanvas().winfo_toplevel().attributes("-fullscreen", True)

draw_outline()
generate_blocks()

display.tracer(False)
player = Turtle("square")
player.color("purple")
player.turtlesize(0.9, 8, 1)
player.hideturtle()
player.penup()
player.goto(0, -280)
player.showturtle()

ball = Turtle("circle")
ball.penup()
ball.color("purple")

start_instruction = Turtle()
start_instruction.color("white")
start_instruction.hideturtle()
start_instruction.penup()
start_instruction.goto(0, 50)
start_instruction.write("Press Space to Start Game", align="center", font=("Fixedsys", 35, "bold"))

scoreboard = Turtle()
scoreboard.color("white")
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(-620, 195)
scoreboard.write(f"SCORE\n {score}", align="center", font=("Fixedsys", 70, "bold"))
display.tracer(True)

display.onkeypress(start_game, "space")
display.onkeypress(display.bye, "Escape")
display.onkey(move_left, "Left")
display.onkey(move_right, "Right")
display.listen()

display.mainloop()
