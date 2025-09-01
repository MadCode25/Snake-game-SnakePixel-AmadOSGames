import turtle
import time
import random

delay = 0.1

# Score

score = 0
high_score = 0


wn = turtle.Screen()
wn.title("SnakePixel | AmadOS Games")
wn.bgcolor("green")
# Set up the screen
wn.setup(width=600, height=600)
# Defines for the head and segments
wn.addshape("Snake_Head.gif")
wn.addshape("Snake_Head_Left.gif")
wn.addshape("Snake_Head_Right.gif")
wn.addshape("Snake_Head_Down.gif")
wn.addshape("Snake_Segment.gif")
wn.tracer(0) # Turns off the screen updates


# Pen for the Tip box
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.shape("square")
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, 230)
pen2.write("You can edit the delay by editing this file in VSCode or Notepad.", align="center", font=("Serif", 10, "normal"))


head = turtle.Turtle()
head.speed(0)
head.shape("Snake_Head.gif")
head.color("orange") # You can change the color if you also want.
head.penup()
head.goto(0, 0)
head.direction = "stop"

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Serif", 24, "normal"))



# Snake Food (Apple)

apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("red") # You can change the color if you also want.
apple.penup()
apple.goto(0, 100)

# Functions / Inits (Original value for all movement steps is 20)

def go_up():
    if head.direction != "down":
        head.direction = "up"
        head.shape("Snake_Head.gif")

def go_down():
    if head.direction != "up":
        head.direction = "down"
        head.shape("Snake_Head_Down.gif")

def go_left():
    if head.direction != "right":
        head.direction = "left"
        head.shape("Snake_Head_Left.gif")

def go_right():
    if head.direction != "left":
        head.direction = "right"
        head.shape("Snake_Head_Right.gif")

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard Bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")



# Main Game Loop.
while True:
    wn.update()
    # Check for a collision
    if head.distance(apple) < 20:
        # Move the food to a random spot in the screen
        x = random.randint(-280, 280)
        y = random.randint(-280, 210)
        apple.goto(x, y)
        score += 10
        pen.clear()
        pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Serif", 24, "normal"))

        # Add a segment.
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("Snake_Segment.gif")
        new_segment.color("#FF8C00")
        new_segment.penup()
        segments.append(new_segment)

        if score > high_score:
            high_score = score
            pen.clear()
            pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Serif", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x , y)
    # Check collisions for the border.
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 210 or head.ycor() < -290:
        time.sleep(0.5)
        head.goto(0, 0)
        head.direction = "stop"
        score = 0
        pen.clear()
        pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Serif", 24, "normal"))

        # Hide the segments.
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()



    move()
    # Check for head collision with the segments.
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction = "stop"
            score = 0
            pen.clear()
            pen.write(f"Score: 0 High Score: {high_score}", align="center", font=("Serif", 24, "normal"))
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
    time.sleep(delay)


wn.mainloop()