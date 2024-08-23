import turtle as t
import random


t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

pablo = t.Turtle()
pablo.color("coral")
pablo.shape("turtle")
pablo.speed(0)


def random_walk(distance=50):
    pablo.pensize(6)
    angles = [90, 180, 270, 360]
    for _ in range(0,101):
        pablo.color(random_color())
        angle = random.choice(angles)
        pablo.forward(distance)
        pablo.setheading(angle)


def draw_spirograh(circle_size=100):
    angle = 0
    while angle != 360:
        pablo.color(random_color())
        pablo.circle(circle_size)
        pablo.setheading(angle)
        angle += 5










# screen = t.Screen()
# screen.exitonclick()