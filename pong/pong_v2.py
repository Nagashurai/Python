import turtle

# creating the game window
screen = turtle.Screen()
screen.title("Pong Championship")
screen.bgcolor("green")
screen.setup(width=1000, height=600)

# Left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("orange")
left_paddle.shapesize(stretch_wid=6, stretch_len=2)
left_paddle.penup()
left_paddle.goto(-400, 0)

# Right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("red")
right_paddle.shapesize(stretch_wid=6, stretch_len=2)
right_paddle.penup()
right_paddle.goto(400, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 7
ball.dy = -7

# score functions
left_player = 0
right_player = 0
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("black")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0    Right_player: 0",
             align="center", font=("Times", 24, "bold"))

# movement for both left and right paddles
def left_paddle_up():
    y = left_paddle.ycor()
    y += 40
    left_paddle.sety(y)


def left_paddle_down():
    y = left_paddle.ycor()
    y -= 40
    left_paddle.sety(y)


def right_paddle_up():
    y = right_paddle.ycor()
    y += 5
    right_paddle.sety(y)


def right_paddle_down():
    y = right_paddle.ycor()
    y -= 5
    right_paddle.sety(y)


# Keyboard bindings
screen.listen()
screen.onkeypress(left_paddle_up, "w")
screen.onkeypress(left_paddle_down, "s")

# Created a bot for the up/down action, remove for two players and comment the bot movement below.
# Modify right paddle movement to make a fair game
# screen.onkeypress(right_paddle_up, "Up")
# screen.onkeypress(right_paddle_down, "Down")


while True:
    screen.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border height
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    # score check for left player
    if ball.xcor() > 500:
        ball.goto(0, 0)
        ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Times", 24, "bold"))

    # score check for right player
    if ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Times", 24, "bold"))

    # Paddle to ball collision
    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() - 40):
        ball.setx(360)
        ball.dx *= -1

    if (ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() - 40):
        ball.setx(-360)
        ball.dx *= -1

    # bot player (right side)
    if (ball.ycor() > right_paddle.ycor()):
        right_paddle_up()

    if (ball.ycor() < right_paddle.ycor()):
        right_paddle_down()

