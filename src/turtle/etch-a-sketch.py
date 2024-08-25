import turtle as t
teddy = t.Turtle()

def move_backword():
    teddy.backward(15)

def move_forward():
    teddy.forward(15)

def move_clockwise():
    teddy.right(15)

def move_counter_clockwise():
    teddy.left(15)    

def clear():
    teddy.clear()
    teddy.reset()

screen = t.Screen()
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backword)
screen.onkey(key='a', fun=move_counter_clockwise)
screen.onkey(key='d', fun=move_clockwise)
screen.onkey(key='c', fun=clear)
screen.exitonclick()

