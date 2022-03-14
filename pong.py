# Special thanks to Christian Thompson from FreeCamp.org
# Original idea from Christian Thompson https://christianthompson.com/ and editied version with additional functions by Brandon Cox bpcox@mtu.edu
# This is a basic Pong game with additional functions added by me to pause/exit the game with the possibility of future additions

import turtle


# Screen

s = turtle.Screen()
s.title("Pong Game")
s.bgcolor("black")
s.setup(width=800,height=600)
s.tracer(0)

#Pausing
is_paused = False

# Scoring
score1 = 0
score2 = 0

# Paddles

paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(350, 0)

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(-350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.changex = .5
ball.changey = .5

#Scoring
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0      Player 2: 0", align="center", font=("Courier", 24, "bold"))


def gameExit():
    s.bye()

def paddle1up():
    ycoord = paddle1.ycor() #Getting the initial coordinate of paddle
    ycoord += 20
    paddle1.sety(ycoord)

def paddle1down():
    ycoord = paddle1.ycor()
    ycoord -= 20
    paddle1.sety(ycoord)

def paddle2up():
    ycoord1 = paddle2.ycor()
    ycoord1 += 20
    paddle2.sety(ycoord1)

def paddle2down():
    ycoord1 = paddle2.ycor()
    ycoord1 -= 20
    paddle2.sety(ycoord1)
def gamePause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True

# Listening for keyboard input
s.listen()
s.onkeypress(gamePause, "v")
s.onkeypress(gameExit, "p")
s.onkeypress(paddle1up, "w")
s.onkeypress(paddle1down, "s")
s.onkeypress(paddle2up, "i")
s.onkeypress(paddle2down, "k")

while True:
    if not is_paused:
        s.update()
    else:
        s.update() #Updating such that turtles on screen move
        ball.setx(ball.xcor() + ball.changex) #Random movement in x direction
        ball.sety(ball.ycor() + ball.changey) #Random movement in y direction

        if ball.ycor() > 290: #Handling if ball touches top of screen
            ball.sety(290) #Setting back to 290
            ball.changey *= -1 #Reversing direction

        if ball.xcor() > 390: #Handling if ball touches right of screen
            ball.goto(0, 0) #Resetting game
            ball.changex *= -1 #Reversing direction
            score1 += 1
            score.clear()
            score.write("Player 1: {}      Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "bold"))
    
        if ball.ycor() < -290: #Handling if ball touches bottom of screen
            ball.sety(-290) #Setting back to -290
            ball.changey *= -1 #Reversing direction

        if ball.xcor() < -390: #Handling if ball touches left of screen
            ball.goto(0, 0) #Resetting game
            ball.changex *= -1 #Reversing direction
            score2 += 1
            score.clear()
            score.write("Player 1: {}      Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "bold"))

        if paddle1.ycor() > 250: #Handling if paddle1 reaches bottom of screen
            paddle1.sety(250) #Setting it to 250 

        if paddle1.ycor() < -250: #Handling if paddle1 reaches bottom of screen
            paddle1.sety(-250) #Setting it to -250

        if paddle2.ycor() > 250: #Handling if paddle2 reaches top of screen
            paddle2.sety(250) #Setting it to 250

        if paddle2.ycor() < -250: #Handling if paddle2 reaches bottom of screen
            paddle2.sety(-250) #Setting it to -250

        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 50):
            ball.setx(340)
            ball.changex *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 50):
            ball.setx(-340)
            ball.changex *= -1
