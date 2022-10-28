import time
import turtle
import random
from playsound import playsound

win=turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.tracer(0)



score=0
highscore=0


head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("cyan")
head.penup()
head.goto(0,0)
head.direction = "stop"

food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,200)

pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.write("Score : 0  Highscore : 0",align="center",font= ("calibre",20))




def goup():
    if head.direction!="down":
        head.direction="up"

def godown():
    if head.direction!="up":
        head.direction="down"

def goleft():
    if head.direction!="right":
        head.direction="left"

def goright():
    if head.direction!="left":
        head.direction="right"

def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)

win.listen()
win.onkeypress(goup, "w")
win.onkeypress(godown, "s")
win.onkeypress(goleft, "a")
win.onkeypress(goright, "d")

body =[]

def play():
    sound=["sample.wav","sample2.mp3","sample3.mp3","sample4.mp3","sample5.mp3"]
    x=random.choice(sound)
    playsound(x)



while True:
    win.update()


    if head.ycor() > 290:
        head.goto(head.xcor(),-290)

    if head.ycor() < -290:
        head.goto(head.xcor(),290)

    if head.xcor() > 290:
        head.goto(-290,head.ycor())

    if head.xcor() < -290:
        head.goto(290,head.ycor())

    if head.distance(food)<20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)
        play()



        score+=10
        if score >highscore:
            highscore= score

        pen.clear()
        pen.write("Score : {} Highscore : {}".format(score,highscore),align="center",font= ("calibre",20))

        new_body = turtle.Turtle()
        new_body.shape("square")
        new_body.color("white")
        new_body.speed(0)
        new_body.penup()
        body.append(new_body)

    for index in range(len(body)-1,0,-1):
        x = body[index - 1].xcor()
        y = body[index - 1].ycor()
        body[index].goto(x,y)

    if len(body)>0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)

    move()

    for i in body:
        if i.distance(head) <20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            playsound("sample6.mp3")

            for i in body:
                i.goto(1000,1000)

            body.clear()

            score=0

            pen.clear()
            pen.write("Score : {} Highscore : {}".format(score,highscore),align="center",font= ("calibre",20))

    time.sleep(0.1)


win.mainloop()
