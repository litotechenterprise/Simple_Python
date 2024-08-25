import turtle as t
import random

screen = t.Screen()
width = 500
height = 400
screen.setup(width, height)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
racers = []
colors = ["red", "green", "blue", "purple", "orange", "gray"]

y = 70 
for i in range(0, len(colors)):
    turtle = t.Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto((((width/2) - 30) * -1), y)
    y -= 30
    racers.append(turtle)



if user_bet:
    print("Turtles take your mark....")
    is_race_on = True


while is_race_on:
    for turtle in racers:
        if turtle.xcor() > (width/2) - 20:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won 🤩! The winning color is {winning_color}")
            else:
                print(f"You've lost 😞! The winning color is {winning_color}")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()