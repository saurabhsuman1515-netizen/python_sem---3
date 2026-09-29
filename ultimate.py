import turtle
import math
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("pink")

# Turtle setup
t = turtle.Turtle()
t.speed(-20)
t.hideturtle()
t.pensize(1)

colors = ["red", "blue", "lime", "yellow",
          "cyan", "magenta", "orange"]

# Draw heart pattern
for i in range(120):
    t.penup()

    angle = (math.pi * 2 * i) / 120

    x = 16 * (math.sin(angle) ** 3) * 15
    y = (13 * math.cos(angle)
         - 5 * math.cos(2 * angle)
         - 2 * math.cos(3 * angle)
         - math.cos(4 * angle)) * 15

    t.goto(x, y)

    t.color(random.choice(colors))
    t.pendown()

    # Draw small flower/star at each point
    for j in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)

turtle.done()