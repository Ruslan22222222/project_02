from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()



def move_forward():
    tim.forward(10)
    tim.color("red")

def move_back():
    tim.back(10)
    tim.color("blue")

def turn_left():
    tim.left(10)
    tim.color("black")

def turn_right():
    tim.right(10)
    tim.color("grey")    

def clear_paper():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()




screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_paper)

screen.exitonclick()





